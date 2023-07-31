from .utils import Version

class AppVersion(Version):
    version_major = 0
    version_minor = 1
    version_patch = 0

    singleton = Version(version_major, version_minor, version_patch)