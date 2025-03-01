from flask import Flask, render_template, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from io import BytesIO

app = Flask(__name__)

def check_url_details(page_url, target_url, anchor_text, expected_rel):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        response = requests.get(page_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        target_links = soup.find_all('a', href=True)
        
        anchor_check = False
        rel_check = False
        
        for link in target_links:
            link_href = link.get('href')
            link_text = link.find(string=re.compile(anchor_text.strip()))
            
            if link_href and (target_url in link_href) and link_text:
                anchor_check = True
                
                rel_value = link.get('rel')
                if rel_value:
                    actual_rel = ' '.join(rel_value).lower()
                else:
                    actual_rel = 'follow'
                
                rel_check = expected_rel.lower() in actual_rel
                break
        
        return {
            'status_code': response.status_code,
            'anchor_check': anchor_check,
            'rel_check': rel_check,
            'error': None
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'status_code': getattr(e.response, 'status_code', None),
            'anchor_check': False,
            'rel_check': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'status_code': None,
            'anchor_check': False,
            'rel_check': False,
            'error': str(e)
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_urls():
    data = request.get_json()
    results = []
    
    for item in data['urls']:
        result = check_url_details(
            item['pageUrl'],
            item['targetUrl'],
            item['anchorText'],
            item.get('expectedRel', '')
        )
        results.append(result)
    
    return jsonify(results)
@app.route('/about')
def about():
    return jsonify({
        "developer": "@ref-N@ghizade",
    })


@app.route('/download-excel', methods=['POST'])
def download_excel():
    try:
        data = request.get_json()
        

        df = pd.DataFrame(data['urls'])
        

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(
                writer,
                index=False,
                sheet_name='URLs',
                columns=['pageUrl', 'targetUrl', 'anchorText', 'expectedRel'],
                header=['Page URL', 'Target URL', 'Anchor Text', 'Expected Rel']
            )
        
        output.seek(0)
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='url_data.xlsx'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
