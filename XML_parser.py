import xml.etree.ElementTree as ET
import time
import pprint
import re
start_time = time.time()

# netinformatie_Obsurv_GM1525
# netinformatie_Obsurv_GM0503

file_path = 'Sample.xml'
parser = ET.XMLParser(encoding='UTF-8')
context = ET.iterparse(file_path, events=(
    "start", "end", "start-ns", "end-ns"), parser=parser)


ns = {'xlink': 'http://www.w3.org/1999/xlink',
      'imkl': 'http://www.geostandaarden.nl/imkl/2015/wion/1.2',
      'gml': 'http://www.opengis.net/gml/3.2',
      'gml:id': 'ID_Netinformatie_GM1525_09-01-2020',
      'us-net-common': 'http://inspire.ec.europa.eu/schemas/us-net-common/4.0'}


# Strip all namespaces from xml to make life much easier. The inclusion of the .xsd file might remove the need for this function
def strip_tag_namespace(t):
    idx = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


def check_valid(input):
    if input != "" and input is not None and input.isprintable():
        return True
    else:
        return False


# This Function needs a lot of work, too many exceptions to the parser rule

def parse(feature):
    tag = strip_tag_namespace(feature.tag)
    sub_1 = '\n'
    #sub_2 = '\t'
    try:
        output = feature.attrib['{' + ns['gml'] + '}id']
        # print(check_valid(output))
        if check_valid(output):
            return output
        else:
            pass
    except:
        pass
    try:
        output = feature.attrib['{' + ns['xlink'] + '}href']
        if check_valid(output):
            return output
        else:
            pass
    except:
        pass
    try:
        output = feature.text
        if check_valid(output):
            return output
        else:
            pass
    except:
        pass


if __name__ == "__main__":

    output = []
    for event, elem in context:
        if event == 'end':
            print(parse(elem))


print("--- %s minutes ---" % ((time.time() - start_time)/60))

# ns1 = {xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance",
# xmlns:gml="http://www.opengis.net/gml/3.2",
# xmlns:base="http://inspire.ec.europa.eu/schemas/base/3.3",
# xmlns:net="http://inspire.ec.europa.eu/schemas/net/4.0",
# xmlns:us-net-ogc="http://inspire.ec.europa.eu/schemas/us-net-ogc/4.0",
# xmlns:us-net-el="http://inspire.ec.europa.eu/schemas/us-net-el/4.0",
# xmlns:us-net-tc="http://inspire.ec.europa.eu/schemas/us-net-tc/4.0",
# xmlns:us-net-common="http://inspire.ec.europa.eu/schemas/us-net-common/4.0",
# xmlns:base2="http://inspire.ec.europa.eu/schemas/base2/2.0",
# xmlns:us-net-sw="http://inspire.ec.europa.eu/schemas/us-net-sw/4.0",
# xmlns:xlink="http://www.w3.org/1999/xlink",
# xmlns:us-net-wa="http://inspire.ec.europa.eu/schemas/us-net-wa/4.0",
# xmlns:us-net-th="http://inspire.ec.europa.eu/schemas/us-net-th/4.0",
# xmlns:imkl="http://www.geostandaarden.nl/imkl/2015/wion/1.2",
# gml:id="ID_Netinformatie_GM1525_09-01-2020",
# xsi:schemaLocation="http://www.geostandaarden.nl/imkl/2015/wion/1.2  http://register.geostandaarden.nl/gmlapplicatieschema/imkl2015/1.2.1/imkl2015-wion.xsd"}
