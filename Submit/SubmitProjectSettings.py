# Project settings
PROJECT="Morphun"
SUBMIT_TO="GoldenGate Azul Hunter Archer"
MA_PROJECT="Morphun_AzulAssets"
GIT_REPO_URL="https://github.siri.apple.com/cslt/morphun.git"
ARTIFACTORY_URL="https://artifactory.siri.apple.com"

RELEASE_EMAIL_FROM= os.system('git config user.email')

RELEASE_EMAIL_TO="morphun-discussion@group.apple.com"

print "EMAIL:", RELEASE_EMAIL_FROM
