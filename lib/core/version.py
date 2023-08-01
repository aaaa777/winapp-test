from .utils import Version

class AppVersion(Version):
    version_major = 0
    version_minor = 1
    version_patch = 2

    version = Version(version_major, version_minor, version_patch)