import urllib

def construct_query(url, params = None):
    """Function to construct a url from a url and parameters as a dict. Can handle urls with existing parameters"""
    result = urllib.parse.urlparse(url)
    if params:
        join_char = ['?', '&'][bool(result[4])] #Picks the join_char based on whether url parameter string is empty
        return result.geturl() + '{0}{1}'.format(join_char, '&'.join('{0}={1}'.format(k, v) for (k, v) in params.items()))
    return result.geturl()

def test_construct_query():
    #test 1
    url = 'http://random.url'
    params = {'key2': 'val2', 'key3': 'val3'}
    assert construct_query(url, params) == "http://random.url?key2=val2&key3=val3"

    #test 2 - initial '?'
    url = 'http://random.url?'
    params = {'key2': 'val2'}
    assert construct_query(url, params) == "http://random.url?key2=val2"

    #test 3 - initial parameters
    url = 'http://random.url?key1=val1'
    params = {'key2': 'val2', 'key3': 'val3'}
    assert construct_query(url, params) == "http://random.url?key1=val1&key2=val2&key3=val3"


    #test 4 - no additional parameters
    url = 'http://random.url?key1=val1'
    assert construct_query(url) == "http://random.url?key1=val1"

    return None

if __name__ == '__main__':
    test_construct_query()
