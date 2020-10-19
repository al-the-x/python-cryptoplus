from pkg_resources import parse_version
import Crypto
__all__ = ["Cipher","PublicKey","Util","Protocol","Hash","testvectors","SelfTest"]

if parse_version(Crypto.__version__) > parse_version("2.0.1"):
        __all__.append("Random")

__author__ = """Philippe Teuwen"""
__email__ = 'phil@teuwen.org'
__version__ = '1.0.0'

#del parse_version
#del Crypto
