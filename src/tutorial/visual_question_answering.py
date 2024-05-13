'''
Created on May 14, 2024

@author: immanueltrummer
'''
import argparse
import openai


def analyze_image(image_url, question):
    """ Use language model to answer question about image.
    
    Args:
        image_url: URL leading to image.
        question: question about image.
    
    Returns:
        Answer generated by the language model.
    """
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role':'user', 'content':[
                {'type':'text', 'text':question},
                {'type':'image_url', 'image_url':{
                    'url':image_url
                    }
                }]
            }]
        )
    return response.choices[0].message.content


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('imageurl', type=str, help='URL to image')
    args = parser.parse_args()
    
    client = openai.OpenAI()
    
    question = input('Ask about the image!')
    answer = analyze_image(args.imageurl, question)
    print(answer)