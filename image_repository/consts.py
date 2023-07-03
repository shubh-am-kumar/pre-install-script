# Constants
IsPrivateImageRegistry = "isPrivateImageRegistry"
PrivateImageRegistrySecret = "imageRegistrySecret"
PrivateImageRegistry = "imageRegistry"

# Documentation
ImageRegistryText = '''
By default, the images are pulled from `gcr.io/prophecy-share` container registry. If the customer wishes to provide their
own container registry, there are provisions in the helm chart to provide the pull secret and private image registry.
'''

# Prompt
IsPrivateImageRegistryPromt = 'Is cluster image registry private?'
PrivateImageRegistrySecretPromt = 'What is the name of the image pull secret?'
PrivateImageRegistryPromt = 'What is the private image registry suffix?'

# Options
