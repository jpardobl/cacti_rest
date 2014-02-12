import subprocess, logging, simplejson
#from cacti_rest import settings
from cacti_rest.models import Settings


def extract_data(path, resolution, start):    
    
    rrdtool = Settings.objects.get(name="path_rrdtool").value
    cmd = "%s fetch %s AVERAGE -r %d -s %s" % (rrdtool, path, resolution, start)
    logging.debug("cmd: %s" % cmd)
    return subprocess.check_output([rrdtool, "fetch", path, "AVERAGE", "-r", str(resolution), "-s", start])


def convert_to_json(data):
    d = []
    for line in data.split("\n"):
        try:
	    time, val = line.split(":")
            time = time.strip()
            val = val.strip()        
            d.append({"timestamp": time, "value": val})
        except ValueError, er: continue
    return d
