
import numpy
from csv import reader
from numpy import linalg as la
import math
w = numpy.array([[-2.66429389e-04, 2.66429389e-04],
                      [3.11439319e-04, -3.11439319e-04],
                      [3.34584666e-04, -3.34584666e-04],
                      [-3.96054276e-04, 3.96054276e-04],
                      [8.75385828e-05, -8.75385828e-05],
                      [2.08986420e-04, -2.08986420e-04],
                      [6.20009491e-05, -6.20009491e-05],
                      [-4.83641543e-04, 4.83641543e-04]])


def calculateG(cluster, train, num_feature, array):
    cluster_center = []
    index = 0
    for i in range(0, cluster):
        list = []
        for j in range(0, num_feature):
            list.append(array[index])
            index += 1
        cluster_center.append(list)
    num_data = len(train)
    g = [[0] * cluster for i in range(num_data)]
    for j in range(0, cluster):
        for i in range(0, num_data):
            sum = 0
            for y in range(0, num_feature):
                sum += (train[i][y] - cluster_center[j][y]) ** 2
            g[i][j] = sum * math.log(math.sqrt(sum))
    return g


def fitness(y, y_net):
    error = 0
    for i in range(0, 2000):
        if (y_net[i][0] < 0):
            error += 1
    for i in range(2000, 4000):
        if (y_net[i][1] < 0):
            error += 1
    precision = 1 - (error / 4000)
    return precision

with open(r'C:\Users\Mohammadreza Rahmani\Desktop\embedding_result.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)

train_data = numpy.array(list_of_rows)
train = []
for item in train_data:
    b = numpy.asarray(item, dtype=numpy.float64, order='C')
    train.append(list(b))

train = train[2000:4000] + train[101999:103999]
array = [[11.706021625759861, -66.39687708363044, 1.5621182209435136, -69.88799261764693, -25.741090760801068,
               45.464799034042464, -6.333581992942967, 11.825284622952966, -15.055416285067663, -25.01041843469035,
               71.98508715763727, -22.749637232125156, 27.989285291988946, -8.491811758242637, 5.775315758794463,
               -23.892423100205338, 21.114617653513328, 81.6557556830671, 39.85751668007405, -40.888915985884466,
               -27.054448156354997, 60.42201321555541, 75.57020824807134, -42.912826964470916, 36.24634296243193,
               89.75755721522454, -11.41153233661361, -14.900446997542923, 55.91964977545724, 60.953404708074665,
               -12.501711666181905, -12.934856861373643, -26.75754052015398, 33.109076737879526, 46.91820598079672,
               -18.62767940417444, -31.922261102182095, 65.49784391299787, 8.510339046144242, -55.89013713135239,
               -5.088546693811564, 14.521926064800656, -3.7606658917933955, 53.42955481153663, 19.96131616860185,
               -17.910166753242464, -1.4566986786193319, 4.628987317501101, 61.79300500485656, 15.786894622996803,
               103.61222611778877, 9.704002915829882, 64.05557514948417, -9.095489391048293, -9.127432092273308,
               28.2504506465606, -30.559383332076813, -106.21348801819548, -88.25532858128463, -48.136220478329506,
               -63.57109934965307, 16.896997009624098, -85.44432883640967, -19.50947361844584, 23.505485907827847,
               44.676704414096115, 48.39349762303757, -91.84778906965329, -31.80470490411905, 63.46137627706144,
               54.48585256255534, -27.55841193585305, 35.513103308466924, 27.344663574188697, -31.27218674205676,
               33.96586358311716, -17.665071929067793, -42.256480935066705, -8.778419377475252, -49.87245476141811,
               -68.55419936800152, 27.858345365831916, -42.5802053110582, -11.966335218880475, 1.3068974537433016,
               -30.945388085650336, -11.164812510073101, -2.3098944120047427, -91.44121628865376, -77.93670931806135,
               35.887671722575135, -25.69208320050643, -49.61254647257583, 38.169424099313055, -49.9756942900241,
               -25.702849487054852, 64.84107500945224, -100.29126132767301, 15.936389393837763, -87.7231455224138,
               45.127186847391854, -10.248036002893924, -55.974750469581906, -19.563069194323024, 21.137766470163616,
               -31.788185930408197, 47.774385221474596, -31.17531588148523, 20.40320371637797, 48.72399927286691,
               -76.1795090878724, 30.43659153759355, -47.48221059973481, 15.277854305066928, -9.604432699377416,
               -124.47473710875838, -56.8641661019544, 19.356707843754215, -78.70545293430385, -2.995964551444736,
               62.37935053118721, -28.061389896663865, -89.90593150738749, 10.696616844927101, -8.49879003089494,
               -33.320873382408635, 5.407214441068478, -10.782366532266197, 93.29150572899636, -31.129205981764702,
               -15.765451837161107, 4.155900414492293, 51.50034056697475, 13.159464729136587, -24.291111128705897,
               71.12003044064865, 21.76066273573066, -77.54465334339741, 7.559002729792903, 7.819141979916901,
               35.60900311377786, 62.29187341662975, -11.614420771747762, 13.38713779460695, -32.892586114044725,
               -60.12816644576741, 4.235355666227724, 15.45983536466029, -22.751728980672286, 53.60442308355286,
               -20.04711236519633, -20.537164718450132, -35.81356040184445, 37.38625608382927, 38.567171267532046,
               -21.39717924305107, 10.107891329294192, 68.04580996228624, 110.20591811306376, 1.69791649280966,
               25.658154156349475, -27.53181957396283, -4.982954972028996, -66.83381014877058, -5.692851341645809,
               -58.230047105205564, -9.420991423176702, 46.07152973730644, -34.85961042825647, 56.80053063465546,
               41.08329794713061, 12.925032207673203, 87.09800311266741, -6.135728998805147, 4.270248684100621,
               13.163664687657445, 22.252626440512454, -8.99186406947045, -9.538771575503665, -58.05606264062158,
               -59.689837370134306, 144.67612852284387, -40.14917243541055, -13.488736289621048, -20.659493477056987,
               -55.17897380487437, -61.814041910736556, 32.39512566641107, -22.66624156001789, 5.490799953777282,
               -56.22978187965454, 7.3455553050760765, -6.856184724004929, 2.490383537526566, -10.715410952869046,
               35.27099426743666, 38.682326473599716, 66.09239645226863, 2.689364434857969, -22.705771138073292,
               0.8324062509779244, -27.236654208512686, -21.992684326696434, -32.51393196339881, -14.213535679851354,
               -20.457359485474267, -26.710325715889862, -8.476793356465167, 2.155078425642102, 24.09624366121467,
               30.261860025306166, -40.36283159631091, 78.09158753328379, -60.298104754114966, 9.269788828126197,
               -42.618439490672365, -20.5190558887239, 62.94394031902315, 54.15334797564682, 14.671745714017185,
               60.27971473852096, 34.74658436453634, 27.23638744525785, 68.56708954637466, 73.93692603156516,
               -74.42127850497607, -21.8600178394077, -31.99423729751402, -0.8299188386465913, -79.74129025983663,
               85.1276456519984, -22.972038675964246, 22.06491673191523, -31.159809862443655, -24.56151476054148,
               -9.141057287195602, 20.564687137999005, 47.9766869152913, -50.63868348486131, -3.9889751229670702,
               23.887911970556015, -9.206735334385872, 57.904641968459856, -40.452692248072665, 85.64270205177226,
               12.765910360660545, -38.82803149694619, -42.14624130564049, -7.57733542912978, -6.482120968323855,
               -52.653778518455724, 13.2402684377415, -37.70916380890009, 5.493558283473333, -25.958961988283615,
               2.8967188973402593, 11.015174344460826, 74.26773714056361, -46.689274055597, -33.23738380132459,
               39.06383882527704, -31.089599903688583, -62.498805148640436, 89.62119378832003, 3.0295516772555193,
               32.59259567316444, 14.500256130870289, -90.74751106140758, 59.07096761221457, 45.35727275665634,
               43.5244311138763, 12.376549118813267, -7.836649708804513, -41.531863624117456, -100.43405312783696,
               74.58672563617242, 10.349436529181839, 31.311719640968903, 50.73155124352729, 31.595722031820717,
               -17.720850221574832, -4.854511504750492, 12.810935565139221, 40.97120176771426, 43.950791672801216,
               -7.012587888831665, -7.921573646951071, -3.0810058930823674, 48.305298507753335, -26.932969663421826,
               -63.89974760365607, 40.862533369704, 45.10406248024378, -5.0064713339449325, -75.33194536219044,
               10.029010473151562, 11.226904564832742, 22.213561659961673, -32.617896845514906, -79.12427490773153,
               28.166317351174, 63.18396172692148, 43.31088820535898, 42.97768008929588, 20.42879031132178,
               90.91929176316489, -20.110894765019253, -34.66551206362329, -8.412589771121697, -66.78809288513006,
               -0.6159827135185308, -8.307817663967986, 19.58777798183497, 21.064740136646503, 42.463253132458185,
               -77.6977267581206, -34.33150380360789, -28.57493844524111, 31.413558938158104, 14.750102910207579,
               -35.557624420078206, -42.49953776700114, -55.63300580715413, -42.68966723188233, 12.337352017765534,
               70.47208201301278, 23.0065370065766, 93.81661152729741, -10.984036784318173, 24.793954361739175,
               33.661850775666316, -17.203513959517128, -56.99876446310709, -7.621387353450309, 34.41891514464272,
               -10.128300137136016, -39.27876140212679, 5.267399968167098, -31.940148258132293, -34.20610721396107,
               -28.339648441999586, -40.6126491546519, 1.5398499690845313, -23.35541050597715, 20.973505635769094,
               -45.53875176896759, 25.95348316493628, -32.298636948083754, 8.187180735092053, 21.476495600526537,
               -82.40159031946617, -14.174620224981588, 42.52953628238959, 10.103444068030743, 57.162038000174576,
               -8.45616146468167, -30.636651699820188, -3.7345783673427593, -11.931406415178852, -4.562516591710769,
               1.84846754848645, -48.319958313021665, -28.344899673839524, -64.17332571359326, -47.01663206751712,
               71.04046907964636, -15.457111433682766, -36.11253355018396, -34.346551631413426, 22.136900731834128,
               -27.07639988376538, -16.37680041666832, -41.127414717017984, -42.58485046012225, 61.468958210028184,
               -21.262686143172996, -12.300793332953281, -1.9807954904725262, -31.22467778054741, -13.033809915499356,
               -26.023675833900743, -33.54627781203508, -0.19808546579833153, 18.63673565809061, 23.58859045547742,
               -39.965085209851374, 10.801436980831667, 4.960767156178782, 33.68400471497905, -11.796232125123337,
               26.003775082842825, -17.829381107804863, 65.47035462065767, 24.52164355129794, -27.835932461553917,
               -11.470506981669319, 56.71264793089497, -40.440434145326385, -67.73554875242621, -51.0525243189662,
               -23.79776921910283, -3.5525899521822537, 7.38961278172878, -35.456167605034445, 31.356915234271625,
               -3.5570709611617057, 9.741756600471755, 18.077060998897544, 51.048793848276986, 97.57592571855838,
               34.08596639296805, -51.32577391937211, -6.634223932171171, -10.690255114932809, -4.550260213675328,
               -6.927182929778789, -66.29903594968418, -51.157869117656375, -3.394289303333164, -40.423458063788594,
               -35.72892378993489, 132.8591807968187, -91.23577548493512, -9.090148596598885, 12.213074727385504,
               -35.55043176121561, 8.168344054857275, 53.28876123902599, -64.06152803079664, 38.265197754350346,
               -41.68471335134504, -8.39514131504021, -9.25346198805917, 60.21520178453872, 3.0318099547183257,
               -55.248350541897615, -27.44293213795322, -70.20503551119097, 70.08244292801358, 44.65694690109879,
               4.536414616310797, -15.172693618346042, 28.05868842650629, 20.421339576768215, 26.768264439995185,
               68.05426752057141, -0.2399838134363919, -27.507103777432864, 21.771737582459668, 1.7516831576906053,
               -0.7674982596807169, -42.569296637818354, -14.973352206733434, -10.959297672484977, -19.20704179025438,
               -64.41469706038006, 49.08985323660674, -17.293199629311765, -60.94343126340475, 57.50977028203957,
               -14.934029799447146, 17.03479902480631, 10.165863068349372, 7.507184447353692, 22.72350300299987,
               96.7270451055835, -16.128581057175495, 88.90019070307162, 24.422393589325686, 28.96636445522522,
               6.837424805341827, 55.136158379845426, 82.17873211049613, 53.07390889919742, -43.20676912396785,
               48.30092885313958, 17.439058353171916, -43.15772034954906, 3.364243688948817, 99.36485512380486,
               16.91669352031258, -92.01201797070541, 46.71704132391982, 40.923061719675964, 86.91925643843575,
               -6.821336557216615, 39.09690867717162, -74.39502603772826, 41.56378624101114, -41.731777971282575,
               45.08451870010328, -73.9358461095548, -54.94464187514554, -7.0785161154923495, -71.80798386760901,
               -36.76521829423155, -9.021272159780292, -47.973860928492996, -35.25533656351003, -55.239088752254055,
               1.7267005189066333, -46.94518589110395, 38.65755801803195, -8.177302496640154, -69.61857179017231,
               -22.08138705672646, -58.04295746634205, -35.073939974676684, 18.27442157374413, 14.411999571718416,
               16.068737110092776, 83.02160568335482, 37.840521627540134, -5.5142202209523, -0.14254809895478754,
               50.573967809950155, 9.997218622855272, -1.365447143134156, -9.171280877919648, 10.07327680105725,
               -88.19150281314037, -23.645851232759913, -64.58046485212887, -56.07388508365988, -13.426579301061443,
               -13.90524949435335, 65.28975542258736, -24.668842397883726, -12.945621177954987, 16.64921233224021,
               -99.58691027067225, 57.05833180242362, 40.747573034912485, -68.49930891419335, -16.085276621241324,
               41.262591965794805, -12.046120112742317, 26.12988886931739, 33.10777238955644, 25.299578281391806,
               16.489185548938003, -39.29353531645951, -22.533436441670442, 4.575690740562302, 22.192776946344512,
               -24.727321277747087, 0.581336342394832, -18.626681351341997, 28.523285206408286, -7.216091066630733,
               14.259217921789565, 21.089617107936665, 30.633852679097387, -23.785160241713726, -14.967598061299034,
               -82.37626695391826, 52.60460180581526, -58.573900199689426, 21.058861625959022, -0.9375279019959275,
               -66.83104129859692, 55.35821116377858, 65.36022564417499, 11.433774922491802, -52.13332643075991,
               -86.81087982392744, 39.47019537642797, 81.49785458378075, -59.784755442756094, -68.99142456429442,
               26.146474368463657, 15.961283449483664, -16.640443486283804, 45.56804239886723, -24.52265740765486,
               -2.8163494347641183, -28.340508464885765, 59.48295913252474, -51.483054839432526, -43.27977434235609,
               3.053205821022198, -39.41885132785586, -57.07115325963007, -35.14214096913415, -26.414211375005888,
               -3.585746892575733, 88.679736464191, -37.42224210804228, 77.5559158098323, -8.341133569766756,
               25.665582058990122, -22.33251215169484, -58.13802694393579, 114.39764960232529, 1.615612612148948,
               -7.366117308572715, 13.510284945634432, -49.60391641009008, -11.243064057831653, 30.41898655992184,
               -20.252309837338267, -26.749655724918476, 25.37597240769644, 47.88914236714553, 25.394582271350203,
               14.184332882984705, 3.649137952704446, 17.808445721762173, 0.8130182135439581, -26.199850618376185,
               0.022204159694962075, -55.026970036446656, -45.089392148715376, -62.61619561787367, 21.059640888163074,
               21.493300686507055, -9.254371525585983, -24.634843941175173, -21.042530105201063, 63.07034709564937,
               -5.243778701903215, -18.978047484398704, -4.5983413453675315, 58.885802480547596, -1.0634940042007741,
               35.943585869398234, 89.7809443172637, -55.78991077908933, 35.92239451866818, -90.34906132080586,
               -41.928661399873235, -40.65629595606852, 0.5863246810184526, 40.478550861783276, 33.14506471034844,
               39.80248205940529, -47.27386604231413, -24.018260228547625, -0.14994250037375023, 22.56231810108256,
               23.52619823834191, -92.97857588831286, -78.42582479596885, -2.2861509984752635, -5.432174991411455,
               27.319452407217135, 18.08708822033485, -55.26856114992445, -28.31860630829822, -6.173126300942652,
               24.70512666428791, 11.477213737868244, -19.80829488942676, 11.161698700603452, -26.20929018410409,
               47.26577152397223, -4.410182682685329, -111.91676285596185, 71.76754392273772, 6.766514993172701,
               -86.64369838208674, -27.347776694706788, -37.29381865795478, -26.198293682739454, -40.98472745214956,
               8.8413412464873, 26.898667058685533, 37.038049845275886, -69.75905210315915, -44.665320108573255,
               37.17547335472147, 5.851539666369118, -32.51604664415581, 57.96097458585118, -51.11008427341966,
               54.08737720524671, 43.68349041340735, -9.245809592618865, -41.104975078389245, 13.710062109324625,
               28.590683538059952, -21.60671479298641, -55.95087306316554, 11.149914960013769, -2.1388020918931807,
               -15.852162166692356, -58.54516664961732, -60.23663380775224, -1.5766866419340477, -4.750999521408755,
               43.770329663982245, -7.210878101523304, -68.14105154925808, 10.813579074698492, -47.75387691017772,
               38.829116593049044, 12.462934581235766, -30.152516556311582, 65.19678151208082, 19.878386822295493,
               -53.53378829220919, 10.087853462410632, 30.537695839696624, 10.891507587866824, -106.28467939934306,
               -35.82106778858309, 36.43318793600409, 0.9866862280077776, -17.06445415784358, 15.805508746304383,
               42.16323126858032, -47.832943319419186, 11.927422341058111, 87.0796142073035, 15.094611411555817,
               -82.29851546934115, -5.780378948087273, 55.714258848906276, 18.19718116689136, -20.31036630640384,
               86.6126180293139, -52.63923246612497, -14.439194679374221, -8.057260341514613, -24.489446362467508,
               -27.958039600585973, -28.13390041847562, -11.985522887316398, -0.27473236758839914, -63.81712315624529,
               5.421717456092099, 10.806879009221468, -32.95492268003647, -0.027941170684115196, -75.3382703577916,
               17.03939876951726, 38.31304153109799, 30.8622660276847, -60.68100165436694, 18.408324678933372,
               24.650814244531176, -13.805927232311104, -19.56791207842989, 37.10458661975192, -4.6412777235135145,
               62.72487124029269, -52.26036128274999, -40.74611095582609, -22.120884814338684, -29.5350962752368,
               28.18252080911762, 40.36317939800891, -35.68179879746434, -13.950702618738942, -13.345485049377352,
               -18.576676100732875, 59.50372908124119, -31.45875920923916, 113.22208825033385, -28.804375299038146,
               3.187012545484519, 31.775426191046336, -44.448681964445505, 14.029511841065325, 41.325384026001714,
               -52.43445813475354, 65.99372216036004, -62.22247035665652, -65.68807570687582, -12.70469753776161,
               31.354445272172086, 6.813145190936438, 21.227138805434514, -64.20134040826692, -19.467814577609534,
               1.1572547624319973, -15.916043403118287, -44.54243832602206, -8.28768609101927, -18.531383439005054,
               -2.2135894789970876, 53.302412753529865, 13.777857451711583, -32.29562421874722, -23.980613225203488,
               -17.11316946701472, 36.83399671631455, -38.353853583865586, -82.15035950926283, 7.876991274504889,
               29.91655570558103, 3.823979557706166, 26.553926264293416, 0.8791522058878793, -24.822469548409234,
               -67.04337987359378, 53.212876298257186, -42.227636698968745, 52.13531347927781, 6.843260387375857,
               0.01236033849409822]]
num_class = 2
cluster = 4 * num_class
num_feature = len(train[0])
g = numpy.array(calculateG(cluster, train, num_feature, array[0]))
y_net = numpy.dot(g, w)

y = [[-1] * 2 for i in range(len(train))]
for i in range(0, 2000):
    y[i][0] = 1

for i in range(2000, len(train)):
    y[i][1] = 1

print(fitness(y, y_net))
y_pos=y_net[0:2000]
t=0
for i in range(0,len(y_pos)):
    if y_pos[i][0]>0:
        t+=1
print(t)
#import csv
#with open(r"C:\Users\Mohammadreza Rahmani\Desktop\y_net.csv", "w", newline="") as f:
#	writer = csv.writer(f)
#	writer.writerows(y_net)

