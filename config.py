"""
Configuration file for the NSFW Moderation Bot
Contains all configurable settings and keyword lists
"""

# Bot configuration
BOT_CONFIG = {
    'command_prefix': '!',
    'status_message': 'Monitoring for NSFW content 🛡️',
    'warning_auto_delete_delay': 10,  # seconds
    'keep_alive_interval': 5,  # minutes
}

# Comprehensive list of NSFW keywords to detect and filter
# This list includes various categories of inappropriate content
NSFW_KEYWORDS = [
    # Explicit sexual terms
    'sex', 'porn', 'nude', 'naked', 'dick', 'cock', 'pussy', 'cunt',
    'boobs', 'tits', 'ass', 'butt', 'clit', 'cum', 'orgasm',
    'masturbation', 'masturbate', 'dildo', 'vibrator',
    
    # Sexual acts
    'fuck', 'fucking', 'fucked', 'suck', 'sucking', 'blowjob',
    'handjob', 'fingering', 'penetration', 'intercourse',
    'hardcore', 'softcore', 'erotic', 'arousal', 'climax',
    
    # Adult content categories
    'gangbang', 'threesome', 'orgy', 'swinger', 'fetish',
    'bdsm', 'bondage', 'domination', 'submission',
    
    # Offensive language (strong profanity)
    'shit', 'bitch', 'whore', 'slut', 'bastard', 'damn',
    
    # Adult industry terms
    'milf', 'cougar', 'escort', 'prostitute', 'stripper',
    'webcam', 'camgirl', 'onlyfans', 'premium snap',
    
    # Animated/drawn adult content
    'hentai', 'ecchi', 'doujin', 'yiff', 'furry porn',
    'rule34', 'lewds', 'nsfw art',
    
    # Sexual orientations (when used inappropriately)
    'gay porn', 'lesbian porn', 'bi porn', 'trans porn',
    
    # Drug-related terms
    'weed', 'marijuana', 'cannabis', 'cocaine', 'heroin',
    'meth', 'drugs', 'high', 'stoned', 'dealer',
    
    # Violence and harmful content
    'kill yourself', 'kys', 'suicide', 'self harm', 'cutting',
    'rape', 'murder', 'violence', 'abuse',
    
    # Spam/inappropriate requests
    'nudes', 'send pics', 'dick pic', 'sext', 'sexting',
    'hook up', 'one night stand', 'fwb', 'netflix and chill',
    
    # Additional contextual terms
    'xxx', '18+', 'adults only', 'not safe for work', 'nsfw',
    'explicit', 'mature content', 'sexual content',
    
    # Common leetspeak/alternative spellings
    'pr0n', 'p0rn', 'b00bs', 's3x', 'fck', 'fuk',
    'sh1t', 'btch', 'cnt', 'fkng', 'sxy', 'hrny',
    
    # Inappropriate requests/commands
    'show me', 'send me', 'trade pics', 'swap pics',
    'rate me', 'am i hot', 'do i look', 'sexy pic',
]

# Additional configuration for keyword matching
KEYWORD_CONFIG = {
    'case_sensitive': False,
    'whole_word_only': False,  # Set to True to only match whole words
    'allow_whitelist': True,   # Allow whitelisted users/channels to bypass filter
}

# Whitelisted channels (channel names or IDs where filtering is disabled)
WHITELISTED_CHANNELS = [
    # Add channel names or IDs here if needed
    # 'admin-only',
    # 123456789012345678,
]

# Whitelisted users (user IDs who bypass the filter)
WHITELISTED_USERS = [
    # Add user IDs here if needed
    # 123456789012345678,
]

# Warning messages (can be customized)
WARNING_MESSAGES = [
    "Please keep the conversation family-friendly! 🛡️",
    "That message contained inappropriate content and has been removed. 🚫",
    "Let's maintain a respectful environment for everyone! ✨",
    "Your message was removed for containing inappropriate content. 📝",
]

# Logging configuration
LOGGING_CONFIG = {
    'log_level': 'INFO',
    'log_file': 'bot.log',
    'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'log_deleted_messages': True,
    'log_warnings_sent': True,
}
