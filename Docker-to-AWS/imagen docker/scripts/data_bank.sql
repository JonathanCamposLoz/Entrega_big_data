
create table num_producto(
	product VARCHAR(250),
	cantidad integer
);

INSERT INTO num_producto(product,cantidad) VALUES
	 ('Bank account or service',86206),
	 ('Checking or savings account',55452),
	 ('Consumer Loan',31604),
	 ('Credit card',89190),
	 ('Credit card or prepaid card',65270),
	 ('Credit reporting',140432),
	 ('Credit reporting, credit repair services, or other personal consumer reports',322817),
	 ('Debt collection',275584),
	 ('Money transfer, virtual currency, or money service',13742),
	 ('Money transfers',5354),
	 ('Mortgage',293191),
	 ('Other financial service',1059),
	 ('Payday loan',5543),
	 ('Payday loan, title loan, or personal loan',11607),
	 ('Prepaid card',3819),
	 ('Student loan',55838),
	 ('Vehicle loan or lease',15040),
	 ('Virtual currency',18);
	
create table num_submitted(
	submitted_via VARCHAR(250),
	cantidad integer
);

INSERT INTO num_submitted(submitted_via,cantidad) VALUES
	('Email',408),
	('Fax',20281),
	('Phone',88128),
	('Postal mail',72427),
	('Referral',186840),
	('Web',1103682);

create table num_anio(
	anio VARCHAR(250),
	cantidad integer
);

INSERT INTO num_anio(anio,cantidad) VALUES
	('2011', 2536),
	('2012', 72373),
	('2013', 108217),
	('2014', 153044),
	('2015', 168475);

create table num_issue(
	issue VARCHAR(250),
	cantidad integer
);

INSERT INTO num_issue(issue,cantidad) VALUES
	 ('APR or interest rate',5506),
	 ('Account opening, closing, or management',37961),
	 ('Account terms and changes',484),
	 ('Adding money',202),
	 ('Advertising',126),
	 ('Advertising and marketing',2959),
	 ('Advertising and marketing, including promotional offers',3972),
	 ('Advertising, marketing or disclosures',77),
	 ('Application processing delay',540),
	 ('Application, originator, mortgage broker',17229),
	 ('Applied for loan/did not receive money',345),
	 ('Applying for a mortgage',635),
	 ('Applying for a mortgage or refinancing an existing mortgage',5785),
	 ('Arbitration',349),
	 ('Attempts to collect debt not owed',58234),
	 ('Balance transfer',1117),
	 ('Balance transfer fee',221),
	 ('Bankruptcy',448),
	 ('Billing disputes',15136),
	 ('Billing statement',2619),
	 ('Can''t contact lender',1106),
	 ('Can''t contact lender or servicer',317),
	 ('Can''t repay my loan',8726),
	 ('Can''t stop charges to bank account',510),
	 ('Can''t stop withdrawals from your bank account',236),
	 ('Cash advance',245),
	 ('Cash advance fee',196),
	 ('Charged bank acct wrong day or amt',297),
	 ('Charged fees or interest I didn''t expect',2753),
	 ('Charged fees or interest you didn''t expect',3126),
	 ('Closing an account',6094),
	 ('Closing on a mortgage',4699),
	 ('Closing your account',4904),
	 ('Closing/Cancelling account',6389),
	 ('Collection debt dispute',901),
	 ('Collection practices',1001),
	 ('Communication tactics',38557),
	 ('Confusing or misleading advertising or marketing',319),
	 ('Confusing or missing disclosures',526),
	 ('Cont''d attempts collect debt not owed',60682),
	 ('Convenience checks',149),
	 ('Credit card protection / Debt protection',2728),
	 ('Credit decision / Underwriting',5652),
	 ('Credit determination',3057),
	 ('Credit limit changed',59),
	 ('Credit line increase/decrease',2185),
	 ('Credit monitoring or identity protection',4424),
	 ('Credit monitoring or identity theft protection services',3687),
	 ('Credit reporting',1696),
	 ('Credit reporting company''s investigation',16883),
	 ('Customer service / Customer relations',3504),
	 ('Customer service/Customer relations',283),
	 ('Dealing with my lender or servicer',17630),
	 ('Dealing with your lender or servicer',15208),
	 ('Delinquent account',3218),
	 ('Deposits and withdrawals',22851),
	 ('Disclosure verification of debt',30797),
	 ('Disclosures',49),
	 ('Excessive fees',176),
	 ('False statements or representation',22896),
	 ('Fees',232),
	 ('Fees or interest',8221),
	 ('Forbearance / Workout plans',556),
	 ('Fraud or scam',7493),
	 ('Getting a credit card',6304),
	 ('Getting a line of credit',485),
	 ('Getting a loan',1110),
	 ('Getting a loan or lease',1716),
	 ('Getting the loan',759),
	 ('Identity theft / Fraud / Embezzlement',8481),
	 ('Identity theft protection or other monitoring services',399),
	 ('Improper contact or sharing of info',10068),
	 ('Improper use of my credit report',5580),
	 ('Improper use of your report',41348),
	 ('Incorrect exchange rate',68),
	 ('Incorrect information on credit report',102686),
	 ('Incorrect information on your report',198687),
	 ('Incorrect/missing disclosures or info',202),
	 ('Late fee',3639),
	 ('Lender damaged or destroyed property',3),
	 ('Lender damaged or destroyed vehicle',8),
	 ('Lender repossessed or sold the vehicle',79),
	 ('Lender sold the property',7),
	 ('Loan modification,collection,foreclosure',112309),
	 ('Loan payment wasn''t credited to your account',204),
	 ('Loan servicing, payments, escrow account',77333),
	 ('Lost or stolen check',145),
	 ('Lost or stolen money order',150),
	 ('Making/receiving payments, sending money',7404),
	 ('Managing an account',34895),
	 ('Managing the line of credit',806),
	 ('Managing the loan or lease',20664),
	 ('Managing, opening, or closing account',1194),
	 ('Managing, opening, or closing your mobile wallet account',884),
	 ('Money was not available when promised',3360),
	 ('Money was taken from your bank account on the wrong day or for the wrong amount',156),
	 ('Opening an account',5205),
	 ('Other',14779),
	 ('Other features, terms, or problems',8296),
	 ('Other fee',2198),
	 ('Other service issues',514),
	 ('Other service problem',704),
	 ('Other transaction issues',1491),
	 ('Other transaction problem',2706),
	 ('Overdraft, savings or rewards features',53),
	 ('Overdraft, savings, or rewards features',19),
	 ('Overlimit fee',215),
	 ('Payment to acct not credited',461),
	 ('Payoff process',2315),
	 ('Privacy',489),
	 ('Problem adding money',135),
	 ('Problem caused by your funds being low',4526),
	 ('Problem getting a card or closing an account',608),
	 ('Problem when making payments',7535),
	 ('Problem with a company''s investigation into an existing issue',766),
	 ('Problem with a credit reporting company''s investigation into an existing problem',73335),
	 ('Problem with a lender or other company charging your account',4287),
	 ('Problem with a purchase or transfer',1500),
	 ('Problem with a purchase shown on your statement',15768),
	 ('Problem with additional add-on products or services',305),
	 ('Problem with an overdraft',4),
	 ('Problem with cash advance',48),
	 ('Problem with credit report or credit score',8),
	 ('Problem with customer service',620),
	 ('Problem with fraud alerts or security freezes',6909),
	 ('Problem with overdraft',22),
	 ('Problem with the payoff process at the end of the loan',1060),
	 ('Problems at the end of the loan or lease',2876),
	 ('Problems caused by my funds being low',11845),
	 ('Problems when you are unable to pay',9385),
	 ('Property was damaged or destroyed property',3),
	 ('Property was sold',5),
	 ('Received a loan I didn''t apply for',615),
	 ('Received a loan you didn''t apply for',292),
	 ('Repaying your loan',3820),
	 ('Rewards',2916),
	 ('Sale of account',344),
	 ('Settlement process and costs',8940),
	 ('Shopping for a line of credit',302),
	 ('Shopping for a loan or lease',2029),
	 ('Struggling to pay mortgage',22884),
	 ('Struggling to pay your bill',1486),
	 ('Struggling to pay your loan',4983),
	 ('Struggling to repay your loan',5964),
	 ('Taking out the loan or lease',4371),
	 ('Taking/threatening an illegal action',8860),
	 ('Threatened to contact someone or share information improperly',3456),
	 ('Took or threatened to take negative or legal action',12248),
	 ('Transaction issue',2700),
	 ('Trouble during payment process',30486),
	 ('Trouble using the card',1032),
	 ('Trouble using your card',2493),
	 ('Unable to get credit report/credit score',10859),
	 ('Unable to get your credit report or credit score',7118),
	 ('Unauthorized transactions or other transaction problem',967),
	 ('Unauthorized transactions/trans. issues',1325),
	 ('Unexpected or other fees',1195),
	 ('Unexpected/Other fees',103),
	 ('Unsolicited issuance of credit card',1853),
	 ('Using a debit or ATM card',6145),
	 ('Vehicle was damaged or destroyed the vehicle',48),
	 ('Vehicle was repossessed or sold the vehicle',136),
	 ('Was approved for a loan, but didn''t receive money',25),
	 ('Was approved for a loan, but didn''t receive the money',109),
	 ('Written notification about debt',29786),
	 ('Wrong amount charged or received',585);


create table complaints_max_per_product_issue(
	product VARCHAR(100),
	issue VARCHAR(200),
	count integer
);

INSERT INTO complaints_max_per_product_issue (product,issue,count) VALUES
	 ('Vehicle loan or lease','Managing the loan or lease',5381),
	 ('Student loan','Dealing with my lender or servicer',17630),
	 ('Prepaid card','Unauthorized transactions/trans. issues',1325),
	 ('Payday loan, title loan, or personal loan','Charged fees or interest you didn''t expect',3126),
	 ('Other financial service','Fraud or scam',379),
	 ('Mortgage','Loan modification,collection,foreclosure',112309),
	 ('Money transfer, virtual currency, or money service','Fraud or scam',5987),
	 ('Debt collection','Cont''d attempts collect debt not owed',60682),
	 ('Credit reporting, credit repair services, or other personal consumer reports','Incorrect information on your report',191833),
	 ('Credit card or prepaid card','Problem with a purchase shown on your statement',15768),
	 ('Consumer Loan','Managing the loan or lease',15283),
	 ('Checking or savings account','Managing an account',34895),
	 ('Bank account or service','Account opening, closing, or management',37961);

create table complaints_per_100k_state(
	state VARCHAR(4),
	complaint_count integer,
	full_name VARCHAR(50),
	population integer,
	complaints_per_100k VARCHAR(50)
);

INSERT INTO complaints_per_100k_state (state,complaint_count,full_name,population,complaints_per_100k) VALUES
	 ('AK',1531,'Alaska',732673,208.96),
	 ('AL',17401,'Alabama',5074300,342.92),
	 ('AR',7150,'Arkansas',3045640,234.76),
	 ('AZ',30622,'Arizona',7359200,416.11),
	 ('CA',199148,'California',39029300,510.25),
	 ('CO',22917,'Colorado',5839930,392.42),
	 ('CT',16089,'Connecticut',3626210,443.69),
	 ('DE',6929,'Delaware',1018400,680.38),
	 ('FL',150693,'Florida',22244800,677.43),
	 ('GA',78458,'Georgia',10912900,718.95),
	 ('HI',4456,'Hawá',1441553,309.11),
	 ('IA',5632,'Iowa',3200520,175.97),
	 ('ID',4309,'Idaho',1939030,222.22),
	 ('IL',56426,'Illinois',12582000,448.47),
	 ('IN',16218,'Indiana',6833040,237.35),
	 ('KS',6961,'Kansas',2937150,237.0),
	 ('KY',10005,'Kentucky',4512310,221.73),
	 ('LA',18192,'Luisiana',4590240,396.32),
	 ('MA',25579,'Massachusetts',6981970,366.36),
	 ('MD',40484,'Maryland',6164660,656.71),
	 ('ME',3883,'Maine',1385340,280.29),
	 ('MI',34102,'Míchiga',10034100,339.86),
	 ('MN',15026,'Minnesota',5717180,262.82),
	 ('MO',20971,'Misuri',6177960,339.45),
	 ('MS',8485,'Misisipi',2940060,288.6),
	 ('MT',2236,'Montana',1122870,199.13),
	 ('NC',45388,'Carolina del Norte',10699000,424.23),
	 ('ND',1383,'Dakota del Norte',779261,177.48),
	 ('NE',3975,'Nebraska',1967920,201.99),
	 ('NH',5232,'Nuevo Hampshire',1395230,374.99),
	 ('NJ',53688,'Nueva Jersey',9261700,579.68),
	 ('NM',6239,'Nuevo Méxic',2113340,295.22),
	 ('NV',19236,'Nevada',3177770,605.33),
	 ('NY',100533,'Nueva York',19677200,510.91),
	 ('OH',43494,'Ohio',11756100,369.97),
	 ('OK',9027,'Oklahoma',4019800,224.56),
	 ('OR',14276,'Oregó',4240140,336.69),
	 ('PA',50340,'Pensilvania',12972000,388.07),
	 ('RI',4147,'Rhode Island',1093730,379.16),
	 ('SC',22641,'Carolina del Sur',5282630,428.59),
	 ('SD',1691,'Dakota del Sur',909824,185.86),
	 ('TN',24249,'Tennessee',7051340,343.89),
	 ('TX',124985,'Texas',30029600,416.21),
	 ('UT',9730,'Utah',3380800,287.8),
	 ('VA',41649,'Virginia',8683620,479.63),
	 ('VT',1834,'Vermont',647064,283.43),
	 ('WA',27129,'Washington',7785790,348.44),
	 ('WI',14715,'Wisconsin',5892540,249.72),
	 ('WV',3379,'Virginia Occidental',1775160,190.35),
	 ('WY',1340,'Wyoming',581381,230.49);


create table complaints_per_channel(
	channel VARCHAR(20),
	count integer
);

INSERT INTO complaints_per_channel (channel,count) VALUES
	 ('Email',408),
	 ('Fax',20281),
	 ('Phone',88128),
	 ('Postal mail',72427),
	 ('Referral',186840),
	 ('Web',1103682);


create table complaints_per_product(
	product VARCHAR(100),
	count integer
);

INSERT INTO complaints_per_product (product,count) VALUES
	 ('Bank account or service',86206),
	 ('Checking or savings account',55452),
	 ('Consumer Loan',31604),
	 ('Credit card or prepaid card',154460),
	 ('Credit reporting, credit repair services, or other personal consumer reports',463249),
	 ('Debt collection',275584),
	 ('Money transfer, virtual currency, or money service',19114),
	 ('Mortgage',293191),
	 ('Other financial service',1059),
	 ('Payday loan, title loan, or personal loan',17150),
	 ('Prepaid card',3819),
	 ('Student loan',55838),
	 ('Vehicle loan or lease',15040);


create table complaints_per_year(
	product VARCHAR(20),
	count integer
);

INSERT INTO complaints_per_year(product, count) VALUES
	('2011', 2536),
	('2012', 72373),
	('2013', 108217),
	('2014', 153044),
	('2015', 168475),
	('2016', 191470),
	('2017', 242967),
	('2018', 257333),
	('2019', 274770),
	('2020', 581);


create table top_words_all_complaints(
	word VARCHAR(100),
	count integer
);

INSERT INTO top_words_all_complaints (word,count) VALUES
	 ('credit',755909),
	 ('account',627359),
	 ('report',328030),
	 ('would',318524),
	 ('payment',313602),
	 ('information',312089),
	 ('loan',298666),
	 ('debt',257649),
	 ('bank',248092),
	 ('told',242916),
	 ('received',228203),
	 ('company',224459),
	 ('time',205307),
	 ('card',204246),
	 ('called',199836),
	 ('never',190898),
	 ('payments',181854),
	 ('sent',178563),
	 ('reporting',178148),
	 ('letter',169902);

create table top_words_credit_reporting(
	word VARCHAR(100),
	count integer
);

INSERT INTO top_words_credit_reporting (word,count) VALUES
	 ('credit',333881),
	 ('report',178597),
	 ('account',165365),
	 ('information',142055),
	 ('reporting',111871),
	 ('consumer',71514),
	 ('accounts',69801),
	 ('equifax',51745),
	 ('company',50748),
	 ('payment',47058),
	 ('removed',43631),
	 ('would',43371),
	 ('file',42418),
	 ('late',42179),
	 ('never',41951),
	 ('debt',41679),
	 ('sent',41096),
	 ('inquiry',40649),
	 ('dispute',40425),
	 ('please',39924);

create table top_words_debt_collection(
	word VARCHAR(100),
	count integer
);

INSERT INTO top_words_debt_collection (word,count) VALUES
	 ('debt',175302),
	 ('credit',132352),
	 ('account',105661),
	 ('collection',72452),
	 ('company',71763),
	 ('report',60056),
	 ('received',54367),
	 ('information',54071),
	 ('would',51220),
	 ('call',47027),
	 ('letter',46340),
	 ('called',45880),
	 ('told',44451),
	 ('never',44231),
	 ('phone',42662),
	 ('sent',42356),
	 ('number',38395),
	 ('pay',36745),
	 ('payment',34799),
	 ('amount',33931);

create table top_words_mortgage(
	word VARCHAR(100),
	count integer
);

INSERT INTO top_words_mortgage (word,count) VALUES
	 ('loan',131858),
	 ('mortgage',128688),
	 ('payment',93305),
	 ('would',72087),
	 ('home',61414),
	 ('payments',55117),
	 ('bank',51520),
	 ('told',51437),
	 ('received',49020),
	 ('account',47981),
	 ('time',46534),
	 ('modification',43658),
	 ('company',38687),
	 ('us',37739),
	 ('sent',37558),
	 ('get',36474),
	 ('pay',35270),
	 ('property',34511),
	 ('letter',34505),
	 ('called',34153);