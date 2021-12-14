import gdown

google_ = 'https://drive.google.com/uc?id='
pt_seg_url = '1xOFyGgzuddCHDs3Zg4XxrkAJviRgyoYG'
pt_detect_url = '1-XEb1XPAIAYoVPFJ3rriRA_7XFqMhgV4'
pt_base_url = '1aJcSUYAz-aBzQpcULa7sfrydPQy2oCjT'
gdown.download(google_+pt_seg_url, 'model_final_best.pth', quiet=False)
gdown.download(google_+pt_detect_url, 'best.pt', quiet=False)
gdown.download(google_+pt_base_url, 'base_best.pt', quiet=False)
