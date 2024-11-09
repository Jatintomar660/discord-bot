import requests
from utils import logger
from config import LEETCODE_API_BASE_URL as BASE_URL

class LeetCodeProfileExtractor:
    username: str

    def __init__(self, username: str):
        self.username = username

    def get_profile_stats(self):
        username = self.username
        url = f"{BASE_URL}/userProfile/{username}/"

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logger.debug(f"Response content: {response.content}")
            logger.error(f"Failed to retrieve the profile for {username}.")
            return None


    def format_leetcode_stats(self,stats):
        username=self.username
        markdown = f"""
    **LeetCode Stats: {username}**

    ** 📘 Total Solved:** {stats['totalSolved']} / {stats['totalQuestions']}  
    ** 📗 Easy Solved:** {stats['easySolved']} / {stats['totalEasy']}  
    ** 📙 Medium Solved:** {stats['mediumSolved']} / {stats['totalMedium']}  
    ** 📕 Hard Solved:** {stats['hardSolved']} / {stats['totalHard']}

    **Total Submissions:**
    ** 📘 All: {stats['totalSubmissions'][0]['count']} / {stats['totalSubmissions'][0]['submissions']}
    ** 📗 Easy: {stats['totalSubmissions'][1]['count']} / {stats['totalSubmissions'][1]['submissions']}
    ** 📙 Medium: {stats['totalSubmissions'][2]['count']} / {stats['totalSubmissions'][2]['submissions']}
    ** 📕 Hard: {stats['totalSubmissions'][3]['count']} / {stats['totalSubmissions'][3]['submissions']}

    **Recent Submission:**  
    📝 **{stats['recentSubmissions'][0]['title']}**  
    _Status:_ {stats['recentSubmissions'][0]['statusDisplay']}  
    _Language:_ {stats['recentSubmissions'][0]['lang']}  
        """
        return markdown
    

    def get_stats_message(self):
        stats=self.get_profile_stats()
        message=self.format_leetcode_stats(stats=stats)
        return message
    

if __name__ == "__main__":
    username = "aryaman0098"
    lc_profile_extractor = LeetCodeProfileExtractor(username=username)
    lc_profile_extractor.get_profile_stats()
