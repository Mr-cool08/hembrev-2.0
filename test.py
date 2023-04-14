import wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
wget.download("http://hembrev-1.mrcoolcool.repl.co")