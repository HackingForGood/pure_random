#coding=utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))

CATEGORIES = [{'name': 'category_1', 'value': 'STEEL'}, {'name': 'category_2', 'value': 'ENVIRONMENT AND FORESTS'}, {'name': 'category_3', 'value': 'URBAN DEVELOPMENT AND POVERTY ALLEVIATION'}, {'name': 'category_4', 'value': 'WOMEN AND CHILD DEVELOPMENT'}, {'name': 'category_5', 'value': 'PRIME  MINISTER'}, {'name': 'category_6', 'value': 'COMMUNICATIONS AND INFORMATION TECHNOLOGY'}, {'name': 'category_7', 'value': 'SCIENCE AND TECHNOLOGY'}, {'name': 'category_8', 'value': 'TOURISM AND CULTURE'}, {'name': 'category_9', 'value': 'RAILWAYS'}, {'name': 'category_10', 'value': 'COMMERCE AND INDUSTRY'}, {'name': 'category_11', 'value': 'HUMAN RESOURCE  DEVELOPMENT'}, {'name': 'category_12', 'value': 'LABOUR AND EMPLOYMENT'}, {'name': 'category_13', 'value': 'LAW , JUSTICE AND COMPANY AFFAIRS'}, {'name': 'category_14', 'value': 'HOME AFFAIRS'}, {'name': 'category_15', 'value': 'HOUSING AND URBAN POVERTY ALLEVIATION'}, {'name': 'category_16', 'value': 'OVERSEAS INDIAN AFFAIRS'}, {'name': 'category_17', 'value': 'SCIENCE AND TECHNOLOGY AND EARTH SCIENCES'}, {'name': 'category_18', 'value': 'MINORITY AFFAIRS'}, {'name': 'category_19', 'value': 'CHEMICALS AND FERTILIZERS'}, {'name': 'category_20', 'value': 'NON-CONVENTIONAL ENERGY SOURCES'}, {'name': 'category_21', 'value': 'FINANCE'}, {'name': 'category_22', 'value': 'POWER'}, {'name': 'category_23', 'value': 'WATER RESOURCES'}, {'name': 'category_24', 'value': 'NA'}, {'name': 'category_25', 'value': 'HEAVY INDUSTRIES AND PUBLIC ENTERPRISES'}, {'name': 'category_26', 'value': 'COAL AND MINES'}, {'name': 'category_27', 'value': 'STATISTICS AND PROGRAMME IMPLEMENTATION'}, {'name': 'category_28', 'value': 'COAL'}, {'name': 'category_29', 'value': 'LABOUR'}, {'name': 'category_30', 'value': 'INFORMATION AND BROADCASTING'}, {'name': 'category_31', 'value': 'CORPORATE AFFAIRS'}, {'name': 'category_32', 'value': 'SHIPPING, ROAD TRANSPORT AND HIGHWAYS'}, {'name': 'category_33', 'value': 'SOCIAL JUSTICE AND EMPOWERMENT'}, {'name': 'category_34', 'value': 'ROAD TRANSPORT AND HIGHWAYS'}, {'name': 'category_35', 'value': 'DEFENCE'}, {'name': 'category_36', 'value': 'HEALTH AND FAMILY WELFARE'}, {'name': 'category_37', 'value': 'PARLIAMENTARY  AFFAIRS'}, {'name': 'category_38', 'value': 'PERSONNEL,  PUBLIC  GRIEVANCES  AND  PENSIONS'}, {'name': 'category_39', 'value': 'MINES'}, {'name': 'category_40', 'value': 'DISINVESTMENT'}, {'name': 'category_41', 'value': 'EXTERNAL AFFAIRS'}, {'name': 'category_42', 'value': 'PLANNING'}, {'name': 'category_43', 'value': 'COMPANY AFFAIRS'}, {'name': 'category_44', 'value': 'RURAL DEVELOPMENT'}, {'name': 'category_45', 'value': 'LAW AND JUSTICE'}, {'name': 'category_46', 'value': 'SMALL SCALE INDUSTRIES'}, {'name': 'category_47', 'value': 'PARLIAMENTARY AFFAIRS'}, {'name': 'category_48', 'value': 'ATOMIC ENERGY'}, {'name': 'category_49', 'value': 'INDUSTRIAL DEVELOPMENT'}, {'name': 'category_50', 'value': 'PANCHAYATI   RAJ'}, {'name': 'category_51', 'value': 'TEXTILES'}, {'name': 'category_52', 'value': 'AGRO AND RURAL INDUSTRIES'}, {'name': 'category_53', 'value': 'CONSUMER AFFAIRS, FOOD AND PUBLIC DISTRIBUTION'}, {'name': 'category_54', 'value': 'LABOUR  AND  EMPLOYMENT'}, {'name': 'category_55', 'value': 'CIVIL AVIATION'}, {'name': 'category_56', 'value': 'PERSONNEL, PUBLIC GRIEVANCES AND PENSIONS'}, {'name': 'category_57', 'value': 'TOURISM'}, {'name': 'category_58', 'value': 'TRIBAL AFFAIRS'}, {'name': 'category_59', 'value': 'SHIPPING'}, {'name': 'category_60', 'value': 'HUMAN RESOURCE DEVELOPMENT'}, {'name': 'category_61', 'value': 'CULTURE'}, {'name': 'category_62', 'value': 'PANCHAYATI RAJ'}, {'name': 'category_63', 'value': 'PETROLEUM  AND  NATURAL  GAS'}, {'name': 'category_64', 'value': 'YOUTH AFFAIRS AND SPORTS'}, {'name': 'category_65', 'value': 'EDUCATION'}, {'name': 'category_66', 'value': 'AGRICULTURE'}, {'name': 'category_67', 'value': 'URBAN DEVELOPMENT'}, {'name': 'category_68', 'value': 'FOOD PROCESSING INDUSTRIES'}]

STATUS_LIST = [
{'name': 'status_1', 'value': 'Assented'},
{'name': 'status_2', 'value': 'Negatived'},
{'name': 'status_3', 'value': 'Lapsed'},
{'name': 'status_4', 'value': 'Passed'},
{'name': 'status_5', 'value': 'Removed'},
{'name': 'status_6', 'value': 'Withdrawn'},
{'name': 'status_7', 'value': 'Pending'},]

START_YEAR = "start_year"
END_YEAR = "end_year"
CATEGORY = "category"
STATUS = "status"
CLUSTERS = "clusters"
PRIVATE = "private"
GOVERNMENT = "government"
LOK = "lok"
RAJYA = "rajya"

CLUSTER_RESULTS = []
SELECTED_CLUSTERS = []