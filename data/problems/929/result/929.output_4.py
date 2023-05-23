# @lc app=leetcode id=929 lang=python3
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # To store unique email addresses
        
        for email in emails:
            local_name, domain_name = email.split("@")  # Split email into local name and domain name
            local_name = local_name.split("+")[0]  # Remove everything after the first '+'
            local_name = local_name.replace(".", "")  # Remove all periods ('.') from the local name
            unique_email = local_name + "@" + domain_name  # Recombine local name and domain name
            
            unique_emails.add(unique_email)  # Add the unique email address to the set
        
        return len(unique_emails)  # Return the number of unique email addresses