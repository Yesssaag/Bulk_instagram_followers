#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

USERNAME = "*username*";
PASSWORD = "*password*";
RATE_LIMIT_LIKE_PER_DAY = 2;
RATE_LIMIT_COMMENTS_PER_DAY = 6;
RATE_LIMIT_FOLLOW_PER_DAY = 600;
RATE_LIMIT_UNFOLLOW_PER_DAY = 4;
RATE_LIMIT_LIKE_PER_TAG = 4;
MY_PROXY = '';




bot = InstaBot(
    login=USERNAME,
    password=PASSWORD,
    like_per_day=RATE_LIMIT_LIKE_PER_DAY,
    comments_per_day=RATE_LIMIT_COMMENTS_PER_DAY,
    tag_list=['follow4follow', 'f4f', 'cute'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=RATE_LIMIT_LIKE_PER_TAG,
    follow_per_day=RATE_LIMIT_FOLLOW_PER_DAY,
    follow_time=1 * 999,
    unfollow_per_day=RATE_LIMIT_UNFOLLOW_PER_DAY,
    unfollow_break_min=4,
    unfollow_break_max=5,
    log_mod=0,
    proxy = MY_PROXY,
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
while True:


    mode = 1;
    if mode == 1:
        client = (3550066610) #the client is the instagram ID for whoever you want your botnet to follow you can just google find ig id
        bot = InstaBot(login="user", password="pass")
        bot.follow(client);
        bot.logout();
        time.sleep(30);
        bot = InstaBot(login="user", password="pass");
        bot.follow(client);
        bot.logout(); #basically your repeating the same code except each time your inputting a different username and pass, this way you can login with multiple accounts and follow one account
