import logging as logger

from FormeAPITest.utils import Readconfig


class Initialize:
    url = ""

    def findURL(self, env):
        logger.info("GET ENV = {}".format(env))
        if env == 'Beta':
            url = Readconfig.GetMembersURL('Beta')
        elif env == 'Develop':
            url = Readconfig.GetMembersURL('Develop')
        elif env == 'Production':
            url = Readconfig.GetMembersURL('Production')
        else:
            logger.error("Environment set is not a valid Environment. Cannot get URL")
            url = ""

        return url

    def getURL(self):
        return self.findURL(self, env)
