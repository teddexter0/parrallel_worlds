## FILE: game/newspaper_generator.rpy
## Generate HTML/CSS newspaper and social media posts

init python:
    import os
    
    def generate_newspaper(headline, subheadline, body, date="February 16, 2026"):
        """Generate newspaper article as HTML, render as image"""
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Times New Roman', serif;
                    background: #f9f9f9;
                    margin: 0;
                    padding: 40px;
                }}
                .newspaper {{
                    width: 700px;
                    background: white;
                    padding: 50px;
                    border: 2px solid #000;
                    box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
                    margin: 0 auto;
                }}
                .masthead {{
                    text-align: center;
                    border-bottom: 4px double black;
                    padding-bottom: 15px;
                    margin-bottom: 25px;
                }}
                .masthead h1 {{
                    font-size: 48px;
                    margin: 0;
                    letter-spacing: 3px;
                }}
                .masthead p {{
                    font-size: 12px;
                    margin: 5px 0 0 0;
                    font-style: italic;
                }}
                .date {{
                    text-align: right;
                    font-size: 14px;
                    margin-bottom: 20px;
                }}
                .headline {{
                    font-size: 42px;
                    font-weight: bold;
                    margin-bottom: 15px;
                    line-height: 1.2;
                }}
                .subheadline {{
                    font-size: 20px;
                    font-style: italic;
                    color: #333;
                    margin-bottom: 25px;
                }}
                .body {{
                    font-size: 16px;
                    line-height: 1.8;
                    columns: 2;
                    column-gap: 30px;
                    text-align: justify;
                }}
            </style>
        </head>
        <body>
            <div class="newspaper">
                <div class="masthead">
                    <h1>THE DAILY CHRONICLE</h1>
                    <p>Truth in Every Line Since 1985</p>
                </div>
                <div class="date">{date}</div>
                <div class="headline">{headline}</div>
                <div class="subheadline">{subheadline}</div>
                <div class="body">{body}</div>
            </div>
        </body>
        </html>
        """
        
        ## Save HTML to file
        article_num = renpy.random.randint(1000, 9999)
        filepath = f"game/images/newspapers/article_{article_num}.html"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        return filepath
    
    def generate_social_post(username, content, likes, comments, timestamp="2h ago"):
        """Generate social media post as HTML"""
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {{ 
                    background: #f0f2f5; 
                    padding: 40px;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                }}
                .post {{ 
                    background: white; 
                    border-radius: 12px; 
                    padding: 25px; 
                    max-width: 550px;
                    margin: 0 auto;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
                .header {{
                    display: flex;
                    align-items: center;
                    margin-bottom: 15px;
                }}
                .avatar {{
                    width: 45px;
                    height: 45px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    margin-right: 12px;
                }}
                .username {{ 
                    font-weight: 600; 
                    font-size: 16px;
                    color: #050505;
                }}
                .timestamp {{
                    font-size: 13px;
                    color: #65676b;
                }}
                .content {{ 
                    margin-bottom: 20px; 
                    font-size: 15px;
                    line-height: 1.5;
                    color: #050505;
                }}
                .stats {{ 
                    color: #65676b; 
                    font-size: 14px;
                    padding-top: 15px;
                    border-top: 1px solid #e4e6eb;
                    display: flex;
                    gap: 20px;
                }}
                .stat-item {{
                    display: flex;
                    align-items: center;
                    gap: 6px;
                }}
            </style>
        </head>
        <body>
            <div class="post">
                <div class="header">
                    <div class="avatar"></div>
                    <div>
                        <div class="username">@{username}</div>
                        <div class="timestamp">{timestamp}</div>
                    </div>
                </div>
                <div class="content">{content}</div>
                <div class="stats">
                    <div class="stat-item">❤️ {likes} likes</div>
                    <div class="stat-item">💬 {comments} comments</div>
                </div>
            </div>
        </body>
        </html>
        """
        
        post_num = renpy.random.randint(1000, 9999)
        filepath = f"game/images/newspapers/social_{post_num}.html"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        return filepath

## Usage in script:
## $ article_path = generate_newspaper(
##     "University Student at Center of Controversy",
##     "Anonymous allegations surface online",
##     "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
## )
## scene expression article_path