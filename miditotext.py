from mido import MidiFile

mid = MidiFile('./assets/twinkle.mid')
mididict = []
output = []

# Put all note on/off in midinote as dictionary.
for i in mid:
    if i.type == 'note_on' or i.type == 'note_off' or i.type == 'time_signature':
        mididict.append(i.dict())
# change time values from delta to relative time.
mem1=0
for i in mididict:
    time = i['time'] + mem1
    i['time'] = time
    mem1 = i['time']
# make every note_on with 0 velocity note_off
    if i['type'] == 'note_on' and i['velocity'] == 0:
        i['type'] = 'note_off'
# put note, starttime, stoptime, as nested list in a list. # format is [type, note, time, channel]
    mem2=[]
    if i['type'] == 'note_on':
        mem2.append(i['time'])
        output.append(mem2)
# viewing the midimessages.



for i in range(len(output)):
    output[i] = output[i][0]

output = list(dict.fromkeys(output))

output.reverse()

for i in range(len(output) - 1):
    output[i] -= output[i+1]

output.reverse()

