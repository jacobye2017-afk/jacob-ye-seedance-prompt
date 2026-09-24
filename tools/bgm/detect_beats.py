#!/usr/bin/env python3
"""Portable extraction of the user-tested 2026-09-23 beat detector.

Requires FFmpeg on PATH plus numpy, scipy, matplotlib. Outputs candidate timing,
not confirmed musical meter or phrases. Original audio stays unchanged.
"""
from pathlib import Path
import argparse, csv, json, shutil, subprocess
import numpy as np
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Local candidate beat detection and click preview; listening confirmation required.')
parser.add_argument('input', type=Path, help='Local audio or video; reads first audio stream')
parser.add_argument('--output', required=True, type=Path)
parser.add_argument('--fps', type=int, choices=[24,25,30,50,60], default=30)
parser.add_argument('--cut-targets', default='', help='Comma-separated editorial cut targets in seconds; no automatic phrase detection')
parser.add_argument('--click-until', type=float, help='Optional editorial cutoff for preview clicks; not automatic fade detection')
args = parser.parse_args()
if not args.input.is_file():
    parser.error('Input file does not exist')
if not shutil.which('ffmpeg'):
    parser.error('ffmpeg must be available on PATH')
try:
    cut_targets = [float(v) for v in args.cut_targets.split(',') if v.strip()]
except ValueError:
    parser.error('--cut-targets must be comma-separated seconds')
if any(not np.isfinite(v) or v < 0 for v in cut_targets):
    parser.error('Cut targets must be finite, non-negative seconds')
if args.click_until is not None and (not np.isfinite(args.click_until) or args.click_until <= 0):
    parser.error('--click-until must be a positive finite number')
ROOT = args.output.resolve()
outputs = ['beat-map.json', 'beat-markers.csv', 'beat-click-preview.m4a', 'beat-timeline.png']
if any((ROOT/name).exists() for name in outputs):
    parser.error('Output files already exist; use a fresh output directory')
ROOT.mkdir(parents=True, exist_ok=True)
SR=22050
y=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(args.input.resolve()),'-map','0:a:0','-f','f32le','-ac','1','-ar',str(SR),'pipe:1']),dtype=np.float32)
duration=len(y)/SR
if duration < 5 or not np.isfinite(y).all() or np.max(np.abs(y)) < 1e-7:
    parser.error('Need at least 5 seconds of non-silent finite audio for candidate detection')
if any(v >= duration for v in cut_targets):
    parser.error('Cut targets must be inside the input duration')
click_until = min(args.click_until, duration) if args.click_until is not None else duration
hop=220
freq,t,z=signal.stft(y,SR,nperseg=1024,noverlap=1024-hop,boundary=None)
mag=np.log1p(np.abs(z)*100)
band=(freq>=80)&(freq<=8000)
flux=np.r_[0,np.maximum(np.diff(mag[band],axis=1),0).mean(axis=0)]
flux=np.maximum(signal.savgol_filter(flux,7,2),0)
if np.std(flux) < 1e-9:
    parser.error('No useful rhythmic change detected')
acf=signal.correlate(flux-flux.mean(),flux-flux.mean(),mode='full',method='fft')[len(flux)-1:]
lo,hi=round(60/160*SR/hop),round(60/45*SR/hop)
pk,_=signal.find_peaks(acf[lo:hi])
if not len(pk):
    parser.error('No periodic candidate found in the 45-160 BPM search range')
lag=int(pk[np.argmax(acf[pk+lo])]+lo)
period=lag*hop/SR

# Dynamic-programming beat path. Signal evidence plus a tempo-continuity penalty.
# This identifies a pulse candidate; it does not identify bar downbeats or instruments.
score=np.zeros(len(flux)); prev=np.full(len(flux),-1,dtype=int)
strength=flux/max(np.std(flux),1e-8)
min_gap,max_gap=round(lag*.65),round(lag*1.4)
for i in range(len(flux)):
    a,b=max(0,i-max_gap),i-min_gap+1
    if b>a:
        js=np.arange(a,b)
        candidates=score[js]-80*np.log((i-js)/lag)**2
        best=int(np.argmax(candidates))
        if candidates[best]>0:
            score[i]=candidates[best]
            prev[i]=js[best]
    score[i]+=strength[i]
last_region=np.where((t>=duration-2*period)&(t<=duration-.2))[0]
end=int(last_region[np.argmax(score[last_region])])
path=[]
while end>=0:
    path.append(end); end=int(prev[end])
path=path[::-1]
peaks,_=signal.find_peaks(flux,distance=round(.16*SR/hop),prominence=.15*np.std(flux))
beats=[]
for idx in path:
    near=peaks[np.abs(peaks-idx)<=round(.1*SR/hop)]
    snapped=int(near[np.argmax(flux[near])]) if len(near) else idx
    support=float(flux[snapped]/max(flux.max(),1e-9))
    # Do not pretend the terminal fade has certain beats.
    beats.append({'time':round(float(t[snapped]),3),'strength':round(support,3),'evidence':'attack-aligned' if support>=.35 else 'weak/interpolated'})
beats=list({b['time']:b for b in beats}.values())
beats.sort(key=lambda b:b['time'])
ibis=np.diff([b['time'] for b in beats if b['time']<click_until])
if len(ibis)<2:
    parser.error('Not enough candidate beats before the chosen cutoff')
tempo=60/np.median(ibis)

cuts=sorted(set(min(beats,key=lambda b:abs(b['time']-target))['time'] for target in cut_targets))
result={
    'duration_seconds':round(duration,3),
    'tempo_estimate_bpm':round(float(tempo),1),
    'autocorrelation_bpm':round(60/period,1),
    'beat_interval_median_seconds':round(float(np.median(ibis)),3),
    'tempo_method':'spectral flux autocorrelation and tempo-constrained dynamic programming; no direct listening',
    'meter':'unconfirmed; do not assume 4/4 or label bar downbeats',
    'review_status':'NEEDS_LISTENING_CONFIRMATION',
    'beats':beats, 'candidate_cut_points_seconds':cuts,
    'timeline_fps':args.fps,
    'candidate_cut_points_frames':[{'time':v,'frame':round(v*args.fps),'timeline_seconds':round(round(v*args.fps)/args.fps,6)} for v in cuts],
    'preview_click_until_seconds':click_until,
    'caution':'Algorithmic candidates, not ear-verified beats. Half/double-time ambiguity remains. Cut choices are editorial suggestions, not detected musical phrase boundaries.'
}
(ROOT/'beat-map.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
with (ROOT/'beat-markers.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['beat_number','audio_seconds',f'frame_{args.fps}fps',f'timecode_{args.fps}fps','attack_strength','evidence'])
    for i,b in enumerate(beats,1):
        n=round(b['time']*args.fps); ss,ff=divmod(n,args.fps); mm,ss=divmod(ss,60); hh,mm=divmod(mm,60)
        w.writerow([i,b['time'],n,f'{hh:02}:{mm:02}:{ss:02}:{ff:02}',b['strength'],b['evidence']])

stereo=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(args.input.resolve()),'-map','0:a:0','-f','f32le','-ac','2','-ar','44100','pipe:1']),dtype=np.float32).reshape(-1,2).copy()
for b in beats:
    if b['time']>=click_until or b['evidence']=='weak/interpolated':
        continue
    start=round(b['time']*44100); length=min(round(.032*44100),len(stereo)-start)
    if length<=0:
        continue
    tt=np.arange(length)/44100
    click=.075*np.sin(2*np.pi*1500*tt)*np.exp(-tt/.007)
    stereo[start:start+length]+=click[:,None]
max_peak=float(np.max(np.abs(stereo)))
if max_peak>.98:
    stereo*=.98/max_peak
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar','44100','-ac','2','-i','pipe:0','-c:a','aac','-b:a','192k','-movflags','+faststart',str(ROOT/'beat-click-preview.m4a')],input=stereo.astype(np.float32).tobytes(),check=True)

plt.rcParams['font.family']='DejaVu Sans'
fig,axs=plt.subplots(2,1,figsize=(14,5),sharex=True,gridspec_kw={'height_ratios':[1,1.15]})
xs=np.arange(0,len(y),100)/SR
axs[0].plot(xs,y[::100],color='#4c9272',lw=.5)
axs[0].set_ylabel('Waveform')
axs[1].plot(t,flux/max(flux.max(),1e-9),color='#416485',lw=1)
for b in beats:
    axs[1].axvline(b['time'],color='#79aa92',alpha=.45,lw=.8)
for v in cuts:
    for ax in axs: ax.axvline(v,color='#cc7c16',lw=1.6)
    axs[1].text(v,.98,f'{v:.2f}',rotation=90,ha='right',va='top',fontsize=9)
axs[1].set_ylabel('Audio attack strength'); axs[1].set_xlabel('Seconds')
axs[1].set_xlim(0,duration); axs[1].set_xticks(np.arange(0,duration+1,max(1,round(duration/22))))
for ax in axs:
    ax.axvspan(click_until,duration,color='#999999',alpha=.15)
    ax.grid(axis='x',alpha=.12)
fig.suptitle(f'BGM timing analysis | ~{tempo:.1f} BPM candidate | orange: editorial cut candidates')
fig.tight_layout(); fig.savefig(ROOT/'beat-timeline.png',dpi=160); plt.close(fig)
print(json.dumps({'tempo':result['tempo_estimate_bpm'],'median_interval':result['beat_interval_median_seconds'],'beat_count':len(beats),'cuts':cuts,'review_status':result['review_status']}))
