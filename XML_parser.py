import xml.etree.cElementTree as ET
import time
import pprint
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


# Strip all namespaces from xml to make life much easier. The includion of the .xsd file might remove the need for this function
def strip_tag_namespace(t):
    idx = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


# This fucntion parsers all the elements from the Utiliteitsnet section of the IMKL xml
def Utiliteitsnet_Parse(feature):
    t_less = strip_tag_namespace(feature.tag)
    # if t_less == 'featureMember':
    #     pass
    if t_less == 'Utiliteitsnet':
        Utiliteitsnet = feature.attrib['{' + ns['gml'] + '}id']
        return Utiliteitsnet
    elif t_less == 'utilityNetworkType':
        utilityNetworkType = feature.attrib['{' + ns['xlink'] + '}href']
        return utilityNetworkType
    elif t_less == 'authorityRole':
        authorityRole = feature.attrib['{' + ns['xlink'] + '}href']
        return authorityRole
    elif t_less == 'namespace':
        namespace = feature.text
        return namespace
    elif t_less == 'lokaalID':
        lokaalID = feature.text
        return lokaalID
    elif t_less == 'beginLifespanVersion':
        beginLifespanVersion = feature.text
        return beginLifespanVersion
    elif t_less == 'omschrijving':
        omschrijving = feature.text
        return omschrijving
    elif t_less == 'thema':
        thema = feature.attrib['{' + ns['xlink'] + '}href']
        return thema


# def Appurtanance_Parse(feature):
#     t_less = strip_tag_namespace(feature.tag)
#     if t_less == 'featureMember':
#         pass
#     elif t_less == 'Appurtenance':
#         Appurtenance = feature.attrib['{' + ns['gml'] + '}id']
#         return Appurtenance
#     elif t_less == 'beginLifespanVersion':
#         beginLifespanVersion = feature.text
#         return beginLifespanVersion
#     elif t_less == 'localId':
#         localId = feature.text
#         return localId
#     elif t_less == 'namespace':
#         namespace = feature.text
#         return namespace
#     elif t_less == 'inNetwork':
#         inNetwork = feature.attrib['{' + ns['xlink'] + '}href']
#         return inNetwork
#     elif t_less == 'geometry':
#         for geo in feature.iter():
#             geo_tag = strip_tag_namespace(geo.tag)
#             if geo_tag == 'pos':
#                 point = geo.text
#                 return point
#     elif t_less == 'currentStatus':
#         currentStatus = feature.attrib['{' + ns['xlink'] + '}href']
#         return currentStatus
#     elif t_less == 'validFrom':
#         validFrom = feature.text
#         return validFrom
#     elif t_less == 'verticalPosition':
#         verticalPosition = feature.text
#         return verticalPosition
#     elif t_less == 'appurtenanceType':
#         appurtenanceType = feature.attrib['{' + ns['xlink'] + '}href']
#         return appurtenanceType

# This is the main XML parser function
output = []
for event, elem in context:
    if event == 'end':
        # print(elem.tag)
        if strip_tag_namespace(elem.tag) == 'Utiliteitsnet':
            u_net = ['u_net']
            for tag in elem.iter():
                value = Utiliteitsnet_Parse(tag)
                if value:
                    u_net.append(value)
            output.append(u_net)
            tag.clear()
        # elem.clear()

# elif tag_less == 'Appurtenance':
#     appurt = ['appurt']
#     for tag in elem.iter():
#         value = Appurtanance_Parse(tag)
#         if value:
#             appurt.append(value)
#     output.append(appurt)

# print(output)
# print(len(output))
# pprint.pprint(output)


# This is the output function that needs to be amended within FME
for i, val in enumerate(output):
    if val[0] == 'u_net':
        Util = val[1]
        Util_net = val[2]
        auth = val[3]
        ID_Lok = val[5]
        life = val[6]
        oms = val[7]
        the = val[8]
        print(i, Util, Util_net, auth, ID_Lok, life, oms, the)
# print(n, len(val), Util)
# print(f'{i}:{val}')

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
