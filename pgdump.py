import subprocess

def dump(url):
	return subprocess.Popen(['pg_dump',url],stdout=subprocess.PIPE)

