import logging
import sys

config = {
    'version': 1,
    'root': {
        'level': logging.DEBUG,
        'handlers': ['console']
    },
    'loggers': {
        'console': {
            'level': logging.DEBUG,
            'handlers': ['console'],
            'propagate': False
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': logging.DEBUG,
            'formatter': 'default',
            'stream': sys.stdout,
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s | %(message)s'
        }
    }
}
