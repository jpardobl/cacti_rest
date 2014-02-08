import subprocess, logging
#from cacti_rest import settings
from cacti_rest.models import Settings


def extract_data(path, resolution, start):    
    
    rrdtool = Settings.objects.get(name="path_rrdtool").value
    cmd = "%s fetch %s AVERAGE -r %d -s %s" % (rrdtool, path, resolution, start)
    logging.debug("cmd: %s" % cmd)
    return subprocess.check_output(cmd)