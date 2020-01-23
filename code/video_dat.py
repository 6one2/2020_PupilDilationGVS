import xml.etree.ElementTree as ET
import time

def VideoDat(name: str):
        tree = ET.parse(name)
        root = tree.getroot()
        
        data = []

        for elem in root.iter('ICSVideo'):
            video = {
                'cond': elem.find('Remarks').text,
                'start_t': elem.find('StartDateTime').text,
                'end_t': elem.find('StopDateTime').text,
                'mod_t': elem.find('LastModifiedDateTime').text,
                'filename': elem.find('FileNameWithPath').text.split('\\')[-1]
            }

            data.append(video)

        return data
        
def time_stamp(time_tag: str):
        time_string, dec_s = time_tag.split('.')
        fmt = '%Y-%m-%dT%H:%M:%S'

        time_stamp = time.mktime(time.strptime(time_string, fmt))
#         time_stamp += float(('.'+dec_s))
        time_stamp += int(dec_s)/10**len(dec_s)
        

        return time_stamp


    