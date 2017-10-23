"""
machineBox.io API
"""

import requests
import json

class MachineboxApi:
    """
    Wrapper for machinebox.io API calls
    """
    def __init__(self, url):
        self.machinebox_url = url
        self.json_header = {"Accept" : "application/json; charset=utf-8", "Content-Type" : "application/json; charset=utf-8"}
        self.file_header = {"Accept" : "application/json; charset=utf-8", "Content-Type" : "multipart/form-data; boundary=gc0p4Jq0M2Yt08jU534c0p ;charset=utf-8"}

    def teach_tagbox(self, url, image_id= None, tag=None):
        """
        Add file with tag and id to the tagbox teach endpoint
        """
        teach_tagbox_url = self.machinebox_url + "tagbox/teach"        
        payload =  {'url': url, 'id': image_id, 'tag': tag }
        response = requests.post(teach_tagbox_url, json=payload,  headers=self.json_header)

        return response
    
    
    def check_tagbox(self, filename):
        """
        Check file against the tagbox check endpoint, getting most confident result
        file=@/path/to/image.jpg
        """
        with open(filename, 'rb') as the_image:
            print("posting file:" +filename)
            files = {'file': (filename, the_image, 'application/json')}
            response = requests.post(self.machinebox_url +"tagbox/check", files=files)
        
        print(response.text)
        return self.parse_tag_response(response)

    def parse_tag_response(self, response):
        json_data = response.json()
        json_success = json_data['success']
        if(not json_success):
             return ("Unsuccessful", 1)
        json_tags = json_data['tags']
        json_custom_tags = json_data['custom_tags']
        top_tag = json_tags[0]
        print(top_tag)

        top_custom_tag = json_custom_tags[0]        
        top_result = self.most_confident_tag(top_tag, top_custom_tag)
        return top_result
    

    def most_confident_tag(self, tag1, tag2):
        """Compare two tags' confidence levels 
        and return the most confident"""

        if(tag1['confidence'] > tag2['confidence']):
            return tag1
        elif(tag1['confidence'] < tag2['confidence']):
            return tag2
        else:
            raise Exception(tag1['tag'], tag2['tag'])


        #json_data = response.json()
        #json_success = json_data['success']
        #print(json_success)
        # if(not json_success):
        #     return
        
        # json_tags = json_data['tags']
        # json_custom_tags = json_data['custom_tags']
        # top_tag = json_tags[0]
        # top_custom_tag = json_custom_tags[0]        
        # top_result = self.most_confident_tag(top_tag, top_custom_tag)
        # return top_result
    

if(__name__ == "__main__"):    
    print("nothing in main\n")
    