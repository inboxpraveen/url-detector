
import joblib
from features_extraction import parse_url
import numpy as np

# from features_extraction import LOCALHOST_PATH #DIRECTORY_NAME

def get_prediction_from_url(test_url):
    features_test = parse_url(test_url)

    """
    This is based on the training part ...

    Index:  0, should be for: having_IPhaving_IP_Address
    Index:  1, should be for: URLURL_Length       
    Index:  2, should be for: Shortining_Service  
    Index:  3, should be for: having_At_Symbol    
    Index:  4, should be for: double_slash_redirecting
    Index:  5, should be for: Prefix_Suffix       
    Index:  6, should be for: having_Sub_Domain   
    Index:  7, should be for: SSLfinal_State      
    Index:  8, should be for: Domain_registeration_length
    Index:  9, should be for: Favicon             
    Index: 10, should be for: HTTPS_token         
    Index: 11, should be for: Request_URL         
    Index: 12, should be for: URL_of_Anchor       
    Index: 13, should be for: Links_in_tags       
    Index: 14, should be for: SFH                 
    Index: 15, should be for: Submitting_to_email 
    Index: 16, should be for: Abnormal_URL        
    Index: 17, should be for: age_of_domain       
    Index: 18, should be for: DNSRecord           
    Index: 19, should be for: web_traffic         
    Index: 20, should be for: Google_Index        
    Index: 21, should be for: Statistical_report  
    """
    
    # we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))
    print("Input Features: ",features_test)
    print("Input Shape: ",features_test.shape)
    
    clf = joblib.load('../saved_model/random_forest_model_compressed.pkl')

    pred = clf.predict(features_test)

    return int(pred[0])


def main(url = ""):
    if url:
        return get_prediction_from_url(url)
        # prediction = get_prediction_from_url(url)
        # if prediction == 1:
        #     # print "The website is safe to browse"
        #     print("SAFE")
        # elif prediction == -1:
        #     # print "The website has phishing features. DO NOT VISIT!"
        #     print("PHISHING")
        # return prediction
    else:
        return 1

if __name__ == "__main__":
    pass
