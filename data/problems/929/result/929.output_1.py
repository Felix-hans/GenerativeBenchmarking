# @lc app=leetcode id=929 lang=python3
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # Use a set to store unique email addresses
        
        for email in emails:
            local, domain = email.split('@')  # Split the email address into local and domain parts
            
            local = local.split('+')[0]
            
            local = local.replace('.', '')
            
            normalized_email = local + '@' + domain
            
            unique_emails.add(normalized_email)
        
        return len(unique_emails)