from csv import reader
import numpy
import psycopg2
from numpy import linalg as la
import math

con=psycopg2.connect(
     host="localhost",
     database="postgres",
     user="postgres",
    password="mm123456"
 )

def calculateW(g,y,cluster):
    lam = 0.01
    w = la.inv(g.transpose().dot(g) + lam * numpy.identity(cluster)).dot(g.transpose()).dot(y)
    return w
def calculateG(cluster,train,num_feature,array):
    cluster_center=[]
    index=0
    for i in range(0,cluster):
        list=[]
        for j in range(0,num_feature):
            list.append(array[index])
            index+=1
        cluster_center.append(list)
    num_data = len(train)
    g = [ [0]*cluster for i in range(num_data)]
    for j in range(0,cluster):
        for i in range(0,num_data):
            sum=0
            for y in range(0,num_feature):
                sum+=(train[i][y]-cluster_center[j][y])**2
            g[i][j]=sum*math.log(math.sqrt(sum))
    return g
def main():
    array=[
        [-32.29927168794427, -22.326019425784498, 17.701877198572614, 10.111491779634306, -11.257119234361658,
         -46.981630674371694, 40.2308124130675, 13.721347388864082, -29.84519815875673, -31.271912032409883,
         -58.083124556563035, -43.1029269396086, 40.60592449953796, -9.283445177459166, -59.59537809087931,
         -26.767034753253782, 47.988819001335365, 20.338948577140204, 8.122830436492656, 60.61111526014578,
         3.8783709238892072, -5.647202801525156, 6.7840902372900596, 49.68442691806071, -10.442765483706046,
         9.679906545365059, -28.956796854611355, -3.79859097694581, -73.65842026861277, 79.13458276628049,
         11.067987932716381, -25.151760783709754, 69.97496847810939, 69.13664773437422, 32.99948208283613,
         49.23629213214859, 21.810795800393766, -9.207730718790115, -43.06396539700567, -23.341295060801308,
         -21.904865709866186, -56.89619476074163, 36.74526081771504, 28.301334359097275, 19.130567594779823,
         -14.480149065697635, 47.137784377681804, 57.63926647889678, -4.126965799915701, -56.55670314855421,
         17.34896426321783, -3.1053445764218943, 29.736934048082226, -38.13759519456275, 2.7266336228108243,
         45.07888419678336, -28.453017382750392, 25.545104774229564, 21.207299106612183, -11.774623141127062,
         49.65645825090107, -20.915376296146476, 18.371474216235985, -8.465922405730472, 72.83014795689796,
         -20.90383279107528, -27.106019520240768, 43.63073100967441, 15.44055976557253, 40.89493125417657,
         12.256522050722591, -0.0361496351046189, -17.081515014734855, -3.4376386003669652, -1.3628801217934374,
         -8.130164946802362, -11.86282707691269, 28.826895670393213, -59.79899327346825, -36.63141613724216,
         54.175439196368146, 50.62241581170265, 1.1716003431400517, 10.611876108694348, 106.20732906783695,
         32.9724066379998, -25.57490360736141, -14.377307322464986, 84.84525329160726, 13.748381018278776,
         33.11953884112687, 58.503245980265994, 31.764221871473126, 37.58936390720427, -26.6902139971455,
         45.728756039972446, 28.00533898740744, -40.52399435635144, -2.088016266353373, 22.985514245293707,
         -0.03599017143619717, 21.93521480266778, -40.942952202336826, 10.141444899418223, 15.064453094833413,
         1.2948539573139064, -52.20362486580046, 13.193263698035317, -10.715925794005791, -13.455602082487935,
         33.92087980171644, 21.926398522143472, -92.2513286309182, -2.0730446228364223, -12.992227560875738,
         -24.806916755996713, 152.61308660177087, -25.92518800609722, 19.778358556417086, 15.23593662682228,
         18.91299638194117, -60.73902547470867, -23.374332658975387, -3.875689974345651, 19.240910972669333,
         -31.477766034784402, -38.083686092148945, 13.521556644227575, 131.51646233931078, -66.40643193611585,
         2.355939535054749, -16.052936873785477, -52.31148143610944, 79.3473621552984, -50.03379313540538,
         -14.690766281083768, 120.6545891041747, -41.211193536498435, -13.449143999714678, 50.610680117791595,
         -63.18272843281759, -65.70837561527198, -2.451542011845437, -31.845178853766544, 30.704719506666592,
         -43.93889065132081, 3.076418239220441, 35.28910070916229, -46.59226387859597, -21.776887916225817,
         18.396433062070795, 36.9048522786356, -60.92011267439512, 75.86489112340057, -10.789051397479183,
         -12.192724281044004, -21.874722136641644, 18.21381750184084, 42.66886591491329, -28.798137231903436,
         64.85159068355505, -79.46640372650582, -32.66376273422099, 44.467600291337355, 1.9213096213594454,
         103.60745641006179, -50.61265079303582, 39.73335780503194, -26.50901048731282, 97.37602561220565,
         -30.60910340858375, -23.115582834589123, 18.438480781759274, -61.472502940503524, 0.49019041466411245,
         -72.72994786879505, 12.4549493265472, 52.78591635425412, -14.242682649761408, -28.204489990405552,
         -12.684978566966127, -74.82625224880867, -18.985816828612204, 21.880416954831436, -14.61171672802497,
         10.233089232943527, 21.7198764156121, 56.33274843002395, 14.747735567535523, -10.17088806081799,
         42.80784264948715, 11.768017129327408, 26.111833508951015, -32.92638810940914, 57.363256334020726,
         19.407094887335255, 70.07593629079885, 9.383004407090036, 41.44905882675193, -44.179632082323764,
         22.64639292419259, 18.582365100590373, 87.89105479035163, -13.052959109780572, -17.64774474105914,
         27.456717676704038, -44.388403030661046, -77.33032944368794, -9.257011373402829, -38.14587878403996,
         44.08926709290155, 7.212627064923454, -55.237456140902594, 20.415989128117552, -27.419248288812803,
         56.2532594329403, 35.0593929537839, -37.40395105892673, -14.357869636391808, 6.732894385808816,
         66.29319033053937, 59.81267262764685, 20.08381712762872, -53.67215877437716, -17.594536200343455,
         -12.317384753353013, -27.597204144581507, -11.509940830523002, -42.992808437462514, -99.19862806234923,
         17.21441781691602, 13.372607196930048, -26.016553808573256, 7.018913507980195, 94.2617633185167,
         33.52024219273909, -0.752584719605094, 25.804887752126007, -34.55080110075023, 50.68590799548249,
         14.451809581441431, 37.84550713705821, -24.240488650074887, -15.631103832449652, -41.636331693147575,
         9.776045897705854, -16.80888411519917, -6.231469849374308, 48.01248343398759, 80.77504060932972,
         47.3966913994209, 48.91131801796858, 1.666652100034378, 12.24135345808194, 19.337681512218378,
         53.27851092771013, 74.66936427302426, -41.63463402383915, -19.592771321569998, -5.65047337823102,
         21.497750103554257, -16.208637937287023, 28.153249040006006, -9.815681172605457, 15.968403350697809,
         -63.38578720204715, 3.4828334351379913, 25.63221547324139, 27.22035553123397, -13.584010121930273,
         -14.064068685139471, 9.83889905165946, 44.4420290149827, 51.954676273581825, 37.48899632831406,
         54.05503323171259, -64.9461511282325, 43.873237113305414, -34.78890098641171, -42.78579665645237,
         4.376488970100665, 16.678314782043536, 38.97575954100183, -43.432377415134454, 59.61038332054016,
         29.69539751654542, 35.494613540206416, 5.163704408017988, -1.5308091665334438, 6.352124383802238,
         91.1315864094363, -20.871856618193327, 11.268102058153287, 14.863406788928359, 25.63345270331484,
         -33.97773957933798, -22.16006476826745, -26.754539294513734, 12.625794860049137, 66.1631349284439,
         -31.23411074795253, -28.131181970709935, -44.799666106016645, 37.10078243976099, 9.34832088156106,
         -74.02326305232978, 52.547367208853764, -52.445192987624615, -28.967739837028564, 17.271796741325844,
         -52.73083310868458, -49.556597740877585, -20.65496384605568, 3.0859892023622533, -2.8556213312648264,
         -72.14212323374254, -60.156437289105206, 10.171045941835885, -29.495531493850535, -25.645944686834845,
         -10.485311849762502, -9.764482623158715, -30.350174534042754, 19.92501778720904, 31.720734984940396,
         -10.76883374569592, 30.99548345951596, -46.06285774909798, 50.121509644789484, 35.657863487717655,
         -32.875062917343826, -56.85342875899226, -4.301959965349786, 19.980093887238375, -19.39292890370144,
         -10.564849715365705, -96.95778117348549, -10.11057881357869, -65.12111344035796, -52.07701140163776,
         11.079570954307703, 18.937764525297755, -53.45259163261872, -35.51864174596363, -20.85579011730632,
         -34.70550566527213, 34.71690056556347, -84.82730574776633, 59.958338990378046, 12.640747100321214,
         0.17112267388478833, 0.2286468093882599, 31.884014255748557, 9.042808647142103, 37.40780578763504,
         -75.8074496197414, -9.120147604125524, 38.42965605507673, -23.650995835522842, 72.92177302361101,
         -9.785769338248393, 19.342571253069405, 18.013493531026842, 24.581438613713217, 23.218756270088925,
         -42.22720637762587, -15.36049600302814, -34.53562080569212, 16.94387596616331, 10.286059421464415,
         57.05929771445756, 89.50395011712541, 66.22889773906455, -13.172038791537217, 2.884266486827155,
         121.00964520791875, 56.29710347749036, 3.0640653322117783, 59.29713295112609, 57.52188352620005,
         -18.0457997674578, 6.786596725370463, 14.053223754078696, -39.03178522536895, -7.5387386432149786,
         -63.472364526155395, -87.48157543768953, 71.9019065921465, -14.297422976107402, 21.289689130878582,
         -16.22268141095253, 76.03183803661517, -22.22052029836831, 66.34888665649109, 32.6405430484792,
         36.72318220489946, 15.804907613991128, 30.5257607425172, 37.31487603801855, 20.778773752374583,
         -0.17597013692178365, 22.05518301818976, -8.645739652023906, -64.58601495155841, -45.651150636704514,
         9.392185208843976, -50.13319827139445, 2.08186344725019, -35.09420175407363, -3.9341917687737316,
         8.411334109595382, 81.93284116536057, 13.713030376828128, -58.477818014926015, 16.36843681875657,
         -20.60933923834308, -10.92916490837362, -47.64446922690044, -2.877416661840619, 6.849128375837188,
         -70.55898457436979, -21.55117544391615, -37.372749507885686, 27.65013998304172, 92.08591571770873,
         -13.895527675759132, -1.4333978877222129, 5.7950757611260535, 57.92692460968274, 8.558371194674892,
         54.010416721233995, 17.694269643708527, 2.829005373278354, 48.496674644757206, 35.301027150262556,
         37.50159710257406, -41.51724747678227, 28.92701617233504, 17.863548024397538, -28.314832560640482,
         30.291815464730377, 99.4583105037051, 106.20775516337564, 15.904896765261308, -45.130128356280274,
         12.800991214838069, 19.637375901201008, 13.438587858267589, -6.8976045997699185, 3.1428166074480206,
         -31.92046476886623, 14.30106591395562, -12.25475125110785, 12.220248838156056, 44.151433178918595,
         25.667409039491524, -41.841507228431496, -33.92902999209436, -14.19765355710537, 26.62494606831277,
         -35.761173392910116, 34.38147122417098, 51.41642479124959, 20.812425760319925, -7.8529917911050084,
         120.16914155337088, -78.54780463089762, -5.724241483114223, 34.76673638106458, 33.893640556502795,
         36.19630799478371, -29.08955331369079, -44.21642239603967, 6.179211109377569, -12.222684663098967,
         52.576685542967496, 36.2903726563211, 7.494641992500163, -6.08486433569583, -0.44504780848588466,
         31.67477490525171, -35.73613401854459, -36.786853319024196, 79.40739118454118, 17.940299470674635,
         -29.85398597219795, 94.90592293444398, -113.25386313631704, -4.530073324846926, -15.571571008213025,
         10.955399624375849, 1.4359112745693405, 58.33157053102346, 18.65985385770901, -15.274352344262905,
         -44.07154631046675, 63.7109069692699, 6.52133635727295, 15.530041169931037, -15.238174040003331,
         30.177619894773475, -52.99626042292577, 52.79808772958754, 20.746404776311234, 19.330431492314435,
         26.896542126180318, 63.552230307675615, 101.26768117653063, -95.56924225962446, 15.531303612766134,
         120.13101918630231, -36.952273027388706, -3.9952379121290282, -60.2506554336657, -29.401652654686067,
         21.867885109356706, 38.74914015475813, 17.085376584460608, -26.694208833837102, -9.070975570507482,
         47.71469308050372, -1.3379113964296132, 26.995769480702304, 119.15025139924899, -39.804993554245414,
         42.697606405117874, -67.61372669048623, 51.532294574116555, -3.5153353445826205, 34.16334559318648,
         -28.146847963974867, -44.23351431374483, 33.985046375069025, 34.68642591083809, 13.508179281897506,
         -37.16240559391882, -40.619798445588835, -7.330155350321218, 6.038894518469269, -11.791327212220269,
         -15.573308497215239, 8.00508662864462, 69.18126855290878, -65.09585743840013, 42.53554915251088,
         -2.253940034179951, 29.219397225516353, 3.1568879950797877, -53.81674409417072, -86.94747642997324,
         47.05563540340171, -31.242616156072057, -34.01650490047487, -34.38820499248918, 17.940304299800403,
         -56.132534135458634, 23.0139649304953, -12.111132995504017, 15.455234865849144, 47.86131091818205,
         -26.60010992023242, 34.57343413610526, 87.6007077924897, -36.06097762786035, -20.985572369949317,
         10.946671369287143, 22.884371094026484, 55.765663712028434, -38.98691598476839, -28.861879262431117,
         10.52643008482614, -31.434599795354025, 15.649467166158669, -24.129501635477613, -4.366601829879482,
         9.400372750257944, 55.39507911338304, -22.396182120372327, 10.256474695297868, 40.97202658555085,
         60.340414903168664, 7.153815377014, 12.98161058268981, -39.099653801777244, -9.024189631202503,
         68.30131872407009, -54.227634669086896, -4.937471479349933, 2.3605351597907736, 36.651740143277934,
         -33.73059806363032, 55.22235289366761, -48.380431365087965, 109.60048320449903, -14.972916877094162,
         35.85929929182798, 41.11017385635102, 20.747576563712535, -11.04698784665926, 33.04088888630233,
         -65.67387000121485, -16.81492906804188, 32.99095146043123, -34.24468266409427, -17.88286137697374,
         -86.51855970918157, 20.801750767436378, -31.874580311288778, -33.298838275068945, -16.43199930226266,
         -41.7730952287106, -3.871545800306425, -33.80381710422998, -42.6577235438873, -3.583937679315677,
         -19.997834237865753, 34.12567630268137, 15.490832270778181, 42.56384393287892, -3.1926353917065335,
         -1.8036467630718782, 16.139291219325532, -28.19014486714507, -32.25597706770032, 55.40132536487303,
         -0.11033990886261837, -77.55749614446881, 41.567537447556646, -29.44148306681311, -2.9382929592254974,
         -50.209845518595806, -26.19060526584689, 25.937206316053622, 24.484430395719738, 4.209786138469848,
         -38.53923379772717, 69.94334084711288, 28.073258899287822, -15.527800035049836, -12.561350940459292,
         -32.889211074438236, 11.209700542696515, 89.28298591666658, -10.141470351575462, -121.30480664313275,
         -45.629404467171916, 19.855999806148866, 16.009539354022582, -18.376286009190192, -38.30464114234124,
         -90.97241761023774, -45.858426909261446, -3.2435923287126482, -75.80110068037023, -101.36536914933691,
         -4.146899888081259, -10.791181802563695, -69.50406637828594, 0.6409032916496243, -38.45285357694622,
         -19.271525030392198, 46.17954240408491, 6.044174843939411, 16.26614948858759, -5.314701775245,
         -28.862692353584983, 52.34867231793719, -43.19574700561008, 90.46880985473534, 21.014556425394485,
         -24.53298079755785, 10.649010984714904, -32.327561826090715, 108.72471165060931, -6.804271502142182,
         -18.49909974666302, -40.47792354773019, 23.945327189834618, 51.71312321853179, 63.45463631196626,
         -2.9303360627664357, 35.7372817190583, 48.558763023570464, -6.0544701095236295, -64.92753563690361,
         -83.06171923092352, 18.17360525617412, -65.46767210457753, -13.888342327392834, 33.34557668353005,
         -10.064110905628723, 15.612169354403802, -30.90910001420479, -54.219143400842725, -13.312463186006202,
         -6.809054093601139, -5.974282954696124, 143.41696057210697, -49.8764518804167, 29.259794731360113,
         55.95769629354336, -22.30169965571761, -27.216739262093913, 59.171494895539006, 59.49318595502737,
         57.679791920456324, 3.4970043867219003, 14.864345392336656, -10.724694686220749, -19.83093471108149,
         4.97526987943256, -47.61353045755878, -20.239165581414543, 36.21160323092501, 83.77243526809825,
         51.377346775086515, -54.285522230502096, -18.494419699574603, -8.54038544479089, 26.661342062876905,
         17.4312246435997, -59.26801452681812, -64.93178852818221, -4.578169799346782, 24.19019072105244,
         0.1976764535067242, -4.574288693420852, -44.66559683518425, -39.39481999037071, -40.1471547258739,
         -53.58660153504176, -34.9467041837892, -19.012435704945325, -34.69882043150891, 9.943694964890778,
         1.5283550836649267, -41.324825034459494, 35.5320594420252, -28.659233466043734, 28.688398513673658,
         64.87856447892798, -2.227421622207218, 60.32092307302291, 17.82931917736519, 3.5450120420891134,
         -42.8006947443091, 29.130068641496862, -36.37431013459573, -23.863585905886282, -13.578374652743491,
         46.75685569968876, 80.5605681800503, 24.534874611029043, -12.0998465308753, -5.095192749472316,
         16.36463481248274, -25.33458076045753, 4.290557088597608, 14.280617585135582, 47.328122373608906,
         22.434109700860322, -70.45968161552516, 34.60755839557723, 0.1359563281681512, 86.40405996332217,
         -17.032893905324517, 4.131999289695894, 32.48848697425144, -34.04505506738921, -62.42275994400861,
         -34.889494623742515, 40.27986272903623, 25.40519611285609, 40.79368984482808, 61.84162200332695,
         -52.17392954551901, 45.37062789463277, -40.55396273477627, -8.265370110663596, 8.553858253089818,
         -43.33636944578868, -15.829968931117309, 8.957309227726766, -22.844941372165984, 78.31782532870135,
         -12.491229330314193, -8.277647284647173, -51.02675600053208, 18.98491442010652, 26.198597367504686,
         24.325519974820892, 30.529661966405236, 24.657474307162374, -11.207845459021714, -41.6314929306658,
         21.384884780166132, 75.08375939925274, -29.09530929094307, -10.862778765205645, 37.2459554557966,
         0.006404922460169929]
    ]
    #print(len(array[0]))
    with open(r'C:\Users\Mohammadreza Rahmani\Desktop\embedding_train.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
    train_data = numpy.array(list_of_rows)
    train = []
    for item in train_data:
        b = numpy.asarray(item, dtype=numpy.float64, order='C')
        train.append(list(b))
    train = train[0:2000] + train[2000:4000]  # increase population
    y = [[-1] * 2 for i in range(len(train))]
    for i in range(0, 2000):
        y[i][0] = 1
    for i in range(2000, len(train)):
        y[i][1] = 1
    num_class = 2
    cluster = 4 * num_class
    num_feature = len(train[0])
    g=numpy.array(calculateG(cluster,train,num_feature,array[0]))
    w = numpy.array(calculateW(g, y, cluster))
    print(w)
    return
main()