# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Fri 21 Jun 2019 18:24:07


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-G',
                order = {'QCD':1})

GC_2 = Coupling(name = 'GC_2',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_3 = Coupling(name = 'GC_3',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_4 = Coupling(name = 'GC_4',
                value = '-(cph*cw*complex(0,1)*gBL)/3.',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(complex(0,1)*Ghaa)',
                order = {'HIG':1})

GC_6 = Coupling(name = 'GC_6',
                value = '-(complex(0,1)*Ghgg)',
                order = {'HIG':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(G*Ghgg)',
                order = {'HIG':1,'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2*Ghgg',
                order = {'HIG':1,'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(CKM1x1*complex(0,1)*gL)/cmath.sqrt(2)',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(CKM1x2*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(CKM1x3*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(CKM2x1*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(CKM2x2*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(CKM2x3*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(CKM3x1*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(CKM3x2*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(CKM3x3*complex(0,1)*gL)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'ct*cw*complex(0,1)*gL',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(complex(0,1)*gL**2)/2.',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-12*complex(0,1)*gL**2',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-12*ct**2*cw**2*complex(0,1)*gL**2',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(CKMp1x1*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CKMp1x2*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CKMp1x3*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKMp2x1*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(CKMp2x2*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CKMp2x3*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKMp3x1*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(CKMp3x2*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKMp3x3*complex(0,1)*gR)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(complex(0,1)*gR**2)/2.',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-12*complex(0,1)*gR**2',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(I14b11/cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((complex(0,1)*I14b11)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(I14b12/cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((complex(0,1)*I14b12)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(I14b13/cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((complex(0,1)*I14b13)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(I14b21/cmath.sqrt(2))',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-((complex(0,1)*I14b21)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(I14b22/cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((complex(0,1)*I14b22)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(I14b23/cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((complex(0,1)*I14b23)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(I14b31/cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((complex(0,1)*I14b31)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(I14b32/cmath.sqrt(2))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((complex(0,1)*I14b32)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(I14b33/cmath.sqrt(2))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((complex(0,1)*I14b33)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(I17b11/cmath.sqrt(2))',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-((complex(0,1)*I17b11)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(I17b12/cmath.sqrt(2))',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-((complex(0,1)*I17b12)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(I17b13/cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((complex(0,1)*I17b13)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(I17b21/cmath.sqrt(2))',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*I17b21)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(I17b22/cmath.sqrt(2))',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*I17b22)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(I17b23/cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*I17b23)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(I17b31/cmath.sqrt(2))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((complex(0,1)*I17b31)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(I17b32/cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((complex(0,1)*I17b32)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(I17b33/cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((complex(0,1)*I17b33)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((complex(0,1)*I20b11)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = 'I20b11/cmath.sqrt(2)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((complex(0,1)*I20b12)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = 'I20b12/cmath.sqrt(2)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((complex(0,1)*I20b13)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = 'I20b13/cmath.sqrt(2)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((complex(0,1)*I20b21)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'I20b21/cmath.sqrt(2)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((complex(0,1)*I20b22)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = 'I20b22/cmath.sqrt(2)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((complex(0,1)*I20b23)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'I20b23/cmath.sqrt(2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((complex(0,1)*I20b31)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'I20b31/cmath.sqrt(2)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((complex(0,1)*I20b32)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = 'I20b32/cmath.sqrt(2)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((complex(0,1)*I20b33)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'I20b33/cmath.sqrt(2)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((complex(0,1)*I5b11)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'I5b11/cmath.sqrt(2)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((complex(0,1)*I5b12)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'I5b12/cmath.sqrt(2)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((complex(0,1)*I5b13)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'I5b13/cmath.sqrt(2)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((complex(0,1)*I5b21)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'I5b21/cmath.sqrt(2)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((complex(0,1)*I5b22)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = 'I5b22/cmath.sqrt(2)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((complex(0,1)*I5b23)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = 'I5b23/cmath.sqrt(2)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((complex(0,1)*I5b31)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = 'I5b31/cmath.sqrt(2)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((complex(0,1)*I5b32)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = 'I5b32/cmath.sqrt(2)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((complex(0,1)*I5b33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = 'I5b33/cmath.sqrt(2)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(gL*gR*kk)/2.',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(complex(0,1)*gL*gR*kk)/2.',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(gL*gR*kk)/2.',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-6*complex(0,1)*lam1',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(complex(0,1)*gL*PMNS1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(complex(0,1)*gL*PMNS1x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(complex(0,1)*gL*PMNS1x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(complex(0,1)*gL*PMNS2x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(complex(0,1)*gL*PMNS2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(complex(0,1)*gL*PMNS2x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(complex(0,1)*gL*PMNS3x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(complex(0,1)*gL*PMNS3x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(complex(0,1)*gL*PMNS3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(complex(0,1)*gR*PMNSp1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(complex(0,1)*gR*PMNSp1x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(complex(0,1)*gR*PMNSp1x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(complex(0,1)*gR*PMNSp2x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(complex(0,1)*gR*PMNSp2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(complex(0,1)*gR*PMNSp2x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '(complex(0,1)*gR*PMNSp3x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(complex(0,1)*gR*PMNSp3x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(complex(0,1)*gR*PMNSp3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = 'cw*complex(0,1)*gR*sph',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-12*cw**2*complex(0,1)*gR**2*sph**2',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cph*cw*complex(0,1)*gBL)/6. - (cw*complex(0,1)*gR*sph)/2.',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(cph*cw*complex(0,1)*gBL)/2. - (cw*complex(0,1)*gR*sph)/2.',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cph*cw*complex(0,1)*gBL)/6. + (cw*complex(0,1)*gR*sph)/2.',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(cph*cw*complex(0,1)*gBL)/2. + (cw*complex(0,1)*gR*sph)/2.',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(cw*complex(0,1)*gL*st)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '12*ct*cw**2*complex(0,1)*gL**2*st',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '-12*cw**2*complex(0,1)*gL**2*st**2',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = 'complex(0,1)*gL*sw',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-12*ct*cw*complex(0,1)*gL**2*sw',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '12*cw*complex(0,1)*gL**2*st*sw',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-12*complex(0,1)*gL**2*sw**2',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(ct*cw*complex(0,1)*gL)/2. - (complex(0,1)*gBL*sph*st)/6. - (cph*ct*complex(0,1)*gBL*sw)/6.',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ct*cw*complex(0,1)*gL)/2. - (complex(0,1)*gBL*sph*st)/6. - (cph*ct*complex(0,1)*gBL*sw)/6.',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(complex(0,1)*gBL*sph*st)/3. + (cph*ct*complex(0,1)*gBL*sw)/3.',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(ct*cw*complex(0,1)*gL)/2. + (complex(0,1)*gBL*sph*st)/2. + (cph*ct*complex(0,1)*gBL*sw)/2.',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ct*cw*complex(0,1)*gL)/2. + (complex(0,1)*gBL*sph*st)/2. + (cph*ct*complex(0,1)*gBL*sw)/2.',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(cw*gR*sph)/2. - (gL*sw)/2.',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cph*cw*complex(0,1)*gBL)/6. - (complex(0,1)*gL*sw)/2.',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(cph*cw*complex(0,1)*gBL)/2. - (complex(0,1)*gL*sw)/2.',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cph*cw*complex(0,1)*gBL)/6. + (complex(0,1)*gL*sw)/2.',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(cph*cw*complex(0,1)*gBL)/2. + (complex(0,1)*gL*sw)/2.',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(cw*gR*sph)/2. + (gL*sw)/2.',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(cph*complex(0,1)*gR*st)/2. - (complex(0,1)*gBL*sph*st)/6. - (cph*ct*complex(0,1)*gBL*sw)/6. - (ct*complex(0,1)*gR*sph*sw)/2.',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cph*complex(0,1)*gR*st)/2. + (complex(0,1)*gBL*sph*st)/2. + (cph*ct*complex(0,1)*gBL*sw)/2. - (ct*complex(0,1)*gR*sph*sw)/2.',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(cph*complex(0,1)*gR*st)/2. - (complex(0,1)*gBL*sph*st)/6. - (cph*ct*complex(0,1)*gBL*sw)/6. + (ct*complex(0,1)*gR*sph*sw)/2.',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(cph*complex(0,1)*gR*st)/2. + (complex(0,1)*gBL*sph*st)/2. + (cph*ct*complex(0,1)*gBL*sw)/2. + (ct*complex(0,1)*gR*sph*sw)/2.',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = 'cph*complex(0,1)*gR*st - ct*complex(0,1)*gR*sph*sw',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(ct*cw*gL)/2. - (cph*gR*st)/2. + (ct*gR*sph*sw)/2.',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-12*cph*cw*complex(0,1)*gR**2*sph*st + 12*ct*cw*complex(0,1)*gR**2*sph**2*sw',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(ct*complex(0,1)*gBL*sph)/6. - (cw*complex(0,1)*gL*st)/2. + (cph*complex(0,1)*gBL*st*sw)/6.',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(ct*complex(0,1)*gBL*sph)/6. + (cw*complex(0,1)*gL*st)/2. + (cph*complex(0,1)*gBL*st*sw)/6.',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ct*complex(0,1)*gBL*sph)/3. - (cph*complex(0,1)*gBL*st*sw)/3.',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(ct*complex(0,1)*gBL*sph)/2. - (cw*complex(0,1)*gL*st)/2. - (cph*complex(0,1)*gBL*st*sw)/2.',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '(ct*complex(0,1)*gBL*sph)/2. + (cw*complex(0,1)*gL*st)/2. - (cph*complex(0,1)*gBL*st*sw)/2.',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(cph*ct*gR)/2. - (cw*gL*st)/2. - (gR*sph*st*sw)/2.',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(cph*ct*complex(0,1)*gR)/2. - (ct*complex(0,1)*gBL*sph)/6. + (cph*complex(0,1)*gBL*st*sw)/6. - (complex(0,1)*gR*sph*st*sw)/2.',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(cph*ct*complex(0,1)*gR)/2. + (ct*complex(0,1)*gBL*sph)/2. - (cph*complex(0,1)*gBL*st*sw)/2. - (complex(0,1)*gR*sph*st*sw)/2.',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(cph*ct*complex(0,1)*gR)/2. - (ct*complex(0,1)*gBL*sph)/6. + (cph*complex(0,1)*gBL*st*sw)/6. + (complex(0,1)*gR*sph*st*sw)/2.',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '(cph*ct*complex(0,1)*gR)/2. + (ct*complex(0,1)*gBL*sph)/2. - (cph*complex(0,1)*gBL*st*sw)/2. + (complex(0,1)*gR*sph*st*sw)/2.',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = 'cph*ct*complex(0,1)*gR + complex(0,1)*gR*sph*st*sw',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-12*cph*ct*cw*complex(0,1)*gR**2*sph - 12*cw*complex(0,1)*gR**2*sph**2*st*sw',
                  order = {'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2)/2. - cw*complex(0,1)*gL*gR*sph*sw + (complex(0,1)*gL**2*sw**2)/2.',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph)/2. + (cph*cw*complex(0,1)*gR**2*sph*st)/2. + (ct*cw*complex(0,1)*gL**2*sw)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw)/2. - (cph*complex(0,1)*gL*gR*st*sw)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2)/2.',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st + (cph**2*complex(0,1)*gR**2*st**2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw - cph*ct*complex(0,1)*gR**2*sph*st*sw + (ct**2*complex(0,1)*gR**2*sph**2*sw**2)/2.',
                  order = {'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '-12*cph**2*complex(0,1)*gR**2*st**2 + 24*cph*ct*complex(0,1)*gR**2*sph*st*sw - 12*ct**2*complex(0,1)*gR**2*sph**2*sw**2',
                  order = {'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '-12*cph**2*cw**2*complex(0,1)*gR**2*sph**2*st**2 + 24*cph*ct*cw**2*complex(0,1)*gR**2*sph**3*st*sw - 12*ct**2*cw**2*complex(0,1)*gL**2*sw**2 - 12*ct**2*cw**2*complex(0,1)*gR**2*sph**4*sw**2',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph)/2. + (cw**2*complex(0,1)*gL*gR*sph*st)/2. - (cph*ct*complex(0,1)*gL*gR*sw)/2. - (cw*complex(0,1)*gL**2*st*sw)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw)/2. - (complex(0,1)*gL*gR*sph*st*sw**2)/2.',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR)/2. - (ct*cw**2*complex(0,1)*gL**2*st)/2. + (cph**2*ct*complex(0,1)*gR**2*st)/2. + (cph*cw*complex(0,1)*gL*gR*st**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw + (cph*complex(0,1)*gR**2*sph*st**2*sw)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2)/2.',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '-12*cph**2*ct*complex(0,1)*gR**2*st + 12*cph*ct**2*complex(0,1)*gR**2*sph*sw - 12*cph*complex(0,1)*gR**2*sph*st**2*sw + 12*ct*complex(0,1)*gR**2*sph**2*st*sw**2',
                  order = {'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '-12*cph**2*ct*cw**2*complex(0,1)*gR**2*sph**2*st + 12*cph*ct**2*cw**2*complex(0,1)*gR**2*sph**3*sw - 12*cph*cw**2*complex(0,1)*gR**2*sph**3*st**2*sw + 12*ct*cw**2*complex(0,1)*gL**2*st*sw**2 + 12*ct*cw**2*complex(0,1)*gR**2*sph**4*st*sw**2',
                  order = {'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st + (cw**2*complex(0,1)*gL**2*st**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw + cw*complex(0,1)*gL*gR*sph*st**2*sw + (complex(0,1)*gR**2*sph**2*st**2*sw**2)/2.',
                  order = {'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '-12*cph**2*ct**2*complex(0,1)*gR**2 - 24*cph*ct*complex(0,1)*gR**2*sph*st*sw - 12*complex(0,1)*gR**2*sph**2*st**2*sw**2',
                  order = {'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '-12*cph**2*ct**2*cw**2*complex(0,1)*gR**2*sph**2 - 24*cph*ct*cw**2*complex(0,1)*gR**2*sph**3*st*sw - 12*cw**2*complex(0,1)*gL**2*st**2*sw**2 - 12*cw**2*complex(0,1)*gR**2*sph**4*st**2*sw**2',
                  order = {'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '-12*cph*cw**3*complex(0,1)*gR**2*sph**3*st + 12*ct*cw**3*complex(0,1)*gR**2*sph**4*sw - 12*ct*cw*complex(0,1)*gL**2*sw**3',
                  order = {'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '-12*cph**3*cw*complex(0,1)*gR**2*sph*st**3 - 12*ct**3*cw**3*complex(0,1)*gL**2*sw + 36*cph**2*ct*cw*complex(0,1)*gR**2*sph**2*st**2*sw - 36*cph*ct**2*cw*complex(0,1)*gR**2*sph**3*st*sw**2 + 12*ct**3*cw*complex(0,1)*gR**2*sph**4*sw**3',
                  order = {'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '-12*cph*ct*cw**3*complex(0,1)*gR**2*sph**3 - 12*cw**3*complex(0,1)*gR**2*sph**4*st*sw + 12*cw*complex(0,1)*gL**2*st*sw**3',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '-12*cph**3*ct*cw*complex(0,1)*gR**2*sph*st**2 + 12*ct**2*cw**3*complex(0,1)*gL**2*st*sw + 24*cph**2*ct**2*cw*complex(0,1)*gR**2*sph**2*st*sw - 12*cph**2*cw*complex(0,1)*gR**2*sph**2*st**3*sw - 12*cph*ct**3*cw*complex(0,1)*gR**2*sph**3*sw**2 + 24*cph*ct*cw*complex(0,1)*gR**2*sph**3*st**2*sw**2 - 12*ct**2*cw*complex(0,1)*gR**2*sph**4*st*sw**3',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '-12*cph**3*ct**2*cw*complex(0,1)*gR**2*sph*st + 12*cph**2*ct**3*cw*complex(0,1)*gR**2*sph**2*sw - 12*ct*cw**3*complex(0,1)*gL**2*st**2*sw - 24*cph**2*ct*cw*complex(0,1)*gR**2*sph**2*st**2*sw + 24*cph*ct**2*cw*complex(0,1)*gR**2*sph**3*st*sw**2 - 12*cph*cw*complex(0,1)*gR**2*sph**3*st**3*sw**2 + 12*ct*cw*complex(0,1)*gR**2*sph**4*st**2*sw**3',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '-12*cph**3*ct**3*cw*complex(0,1)*gR**2*sph - 36*cph**2*ct**2*cw*complex(0,1)*gR**2*sph**2*st*sw + 12*cw**3*complex(0,1)*gL**2*st**3*sw - 36*cph*ct*cw*complex(0,1)*gR**2*sph**3*st**2*sw**2 - 12*cw*complex(0,1)*gR**2*sph**4*st**3*sw**3',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '-12*cw**4*complex(0,1)*gR**2*sph**4 - 12*complex(0,1)*gL**2*sw**4',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '-12*ct**4*cw**4*complex(0,1)*gL**2 - 12*cph**4*complex(0,1)*gR**2*st**4 + 48*cph**3*ct*complex(0,1)*gR**2*sph*st**3*sw - 72*cph**2*ct**2*complex(0,1)*gR**2*sph**2*st**2*sw**2 + 48*cph*ct**3*complex(0,1)*gR**2*sph**3*st*sw**3 - 12*ct**4*complex(0,1)*gR**2*sph**4*sw**4',
                  order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '12*ct**3*cw**4*complex(0,1)*gL**2*st - 12*cph**4*ct*complex(0,1)*gR**2*st**3 + 36*cph**3*ct**2*complex(0,1)*gR**2*sph*st**2*sw - 12*cph**3*complex(0,1)*gR**2*sph*st**4*sw - 36*cph**2*ct**3*complex(0,1)*gR**2*sph**2*st*sw**2 + 36*cph**2*ct*complex(0,1)*gR**2*sph**2*st**3*sw**2 + 12*cph*ct**4*complex(0,1)*gR**2*sph**3*sw**3 - 36*cph*ct**2*complex(0,1)*gR**2*sph**3*st**2*sw**3 + 12*ct**3*complex(0,1)*gR**2*sph**4*st*sw**4',
                  order = {'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '-12*ct**2*cw**4*complex(0,1)*gL**2*st**2 - 12*cph**4*ct**2*complex(0,1)*gR**2*st**2 + 24*cph**3*ct**3*complex(0,1)*gR**2*sph*st*sw - 24*cph**3*ct*complex(0,1)*gR**2*sph*st**3*sw - 12*cph**2*ct**4*complex(0,1)*gR**2*sph**2*sw**2 + 48*cph**2*ct**2*complex(0,1)*gR**2*sph**2*st**2*sw**2 - 12*cph**2*complex(0,1)*gR**2*sph**2*st**4*sw**2 - 24*cph*ct**3*complex(0,1)*gR**2*sph**3*st*sw**3 + 24*cph*ct*complex(0,1)*gR**2*sph**3*st**3*sw**3 - 12*ct**2*complex(0,1)*gR**2*sph**4*st**2*sw**4',
                  order = {'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '-12*cph**4*ct**3*complex(0,1)*gR**2*st + 12*ct*cw**4*complex(0,1)*gL**2*st**3 + 12*cph**3*ct**4*complex(0,1)*gR**2*sph*sw - 36*cph**3*ct**2*complex(0,1)*gR**2*sph*st**2*sw + 36*cph**2*ct**3*complex(0,1)*gR**2*sph**2*st*sw**2 - 36*cph**2*ct*complex(0,1)*gR**2*sph**2*st**3*sw**2 + 36*cph*ct**2*complex(0,1)*gR**2*sph**3*st**2*sw**3 - 12*cph*complex(0,1)*gR**2*sph**3*st**4*sw**3 + 12*ct*complex(0,1)*gR**2*sph**4*st**3*sw**4',
                  order = {'QED':2})

GC_193 = Coupling(name = 'GC_193',
                  value = '-12*cph**4*ct**4*complex(0,1)*gR**2 - 12*cw**4*complex(0,1)*gL**2*st**4 - 48*cph**3*ct**3*complex(0,1)*gR**2*sph*st*sw - 72*cph**2*ct**2*complex(0,1)*gR**2*sph**2*st**2*sw**2 - 48*cph*ct*complex(0,1)*gR**2*sph**3*st**3*sw**3 - 12*complex(0,1)*gR**2*sph**4*st**4*sw**4',
                  order = {'QED':2})

GC_194 = Coupling(name = 'GC_194',
                  value = '-(gL*gR*TH1x1)/2.',
                  order = {'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(complex(0,1)*gL*gR*TH1x1)/2.',
                  order = {'QED':2})

GC_196 = Coupling(name = 'GC_196',
                  value = '(gL*gR*TH1x1)/2.',
                  order = {'QED':2})

GC_197 = Coupling(name = 'GC_197',
                  value = '-(gL*gR*TH1x2)/2.',
                  order = {'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '-(complex(0,1)*gL*gR*TH1x2)/2.',
                  order = {'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '(gL*gR*TH1x2)/2.',
                  order = {'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = '-(gL*gR*TH1x3)/2.',
                  order = {'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '-(complex(0,1)*gL*gR*TH1x3)/2.',
                  order = {'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '(gL*gR*TH1x3)/2.',
                  order = {'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '-(gL*gR*TH1x4)/2.',
                  order = {'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(complex(0,1)*gL*gR*TH1x4)/2.',
                  order = {'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = '(gL*gR*TH1x4)/2.',
                  order = {'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(complex(0,1)*gL**2*TH1x1**2)/2. + (complex(0,1)*gL**2*TH3x1**2)/2.',
                  order = {'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(complex(0,1)*gL**2*TH1x1*TH1x2)/2. + (complex(0,1)*gL**2*TH3x1*TH3x2)/2.',
                  order = {'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(complex(0,1)*gL**2)/2. + (complex(0,1)*gL**2*TH1x2**2)/2. + (complex(0,1)*gL**2*TH3x2**2)/2.',
                  order = {'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(complex(0,1)*gL**2*TH1x1*TH1x3)/2. + (complex(0,1)*gL**2*TH3x1*TH3x3)/2.',
                  order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(complex(0,1)*gL**2*TH1x2*TH1x3)/2. + (complex(0,1)*gL**2*TH3x2*TH3x3)/2.',
                  order = {'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(complex(0,1)*gL**2*TH1x3**2)/2. + (complex(0,1)*gL**2*TH3x3**2)/2.',
                  order = {'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '(complex(0,1)*gL**2*TH1x1*TH1x4)/2. + (complex(0,1)*gL**2*TH3x1*TH3x4)/2.',
                  order = {'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '(complex(0,1)*gL**2*TH1x2*TH1x4)/2. + (complex(0,1)*gL**2*TH3x2*TH3x4)/2.',
                  order = {'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '(complex(0,1)*gL**2*TH1x3*TH1x4)/2. + (complex(0,1)*gL**2*TH3x3*TH3x4)/2.',
                  order = {'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '(complex(0,1)*gL**2*TH1x4**2)/2. + (complex(0,1)*gL**2*TH3x4**2)/2.',
                  order = {'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '-2*complex(0,1)*lam1*TH1x1**2 - 4*complex(0,1)*lam2*TH1x1**2 - 2*alp1*complex(0,1)*TH3x1**2 - 2*alp3*complex(0,1)*TH3x1**2 - 2*alp1*complex(0,1)*TH4x1**2 - 2*alp3*complex(0,1)*TH4x1**2',
                  order = {'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '(complex(0,1)*gR**2*TH1x1**2)/2. + (complex(0,1)*gR**2*TH4x1**2)/2.',
                  order = {'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x1**2)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x1**2 + (complex(0,1)*gL**2*sw**2*TH1x1**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x1**2)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x1**2 + (complex(0,1)*gL**2*sw**2*TH3x1**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x1**2)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x1**2 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x1**2)/2.',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x1**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x1**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x1**2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x1**2)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x1**2)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x1**2)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x1**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x1**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x1**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x1**2)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x1**2)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x1**2)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x1**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x1**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x1**2)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x1**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x1**2)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x1**2 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x1**2)/2.',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x1**2)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x1**2)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x1**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x1**2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x1**2)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x1**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x1**2)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x1**2)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x1**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x1**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x1**2)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x1**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x1**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x1**2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x1**2)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x1**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x1**2)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x1**2 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x1**2)/2.',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x1**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1**2 + (cph**2*complex(0,1)*gR**2*st**2*TH1x1**2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x1**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x1**2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x1**2)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x1**2)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x1**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x1**2)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x1**2)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x1**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x1**2)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1**2 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x1**2)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x1**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x1**2)/2.',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x1**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x1**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x1**2)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x1**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x1**2)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x1**2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x1**2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x1**2)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x1**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x1**2)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x1**2)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x1**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x1**2)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x1**2 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x1**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x1**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x1**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x1**2 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x1**2)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x1**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x1**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x1**2)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x1**2)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x1**2)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x1**2)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x1**2)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x1**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x1**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x1**2 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x1**2)/2.',
                  order = {'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x1**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1**2 + (cw**2*complex(0,1)*gL**2*st**2*TH1x1**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1**2 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x1**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x1**2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x1**2)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1**2 + (cw**2*complex(0,1)*gL**2*st**2*TH3x1**2)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1**2 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x1**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x1**2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x1**2)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x1**2 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x1**2)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1**2 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1**2 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1**2 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x1**2)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x1**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x1**2)/2.',
                  order = {'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '-6*complex(0,1)*lam1*TH1x1**4 - 12*alp1*complex(0,1)*TH1x1**2*TH3x1**2 - 12*alp2*complex(0,1)*TH1x1**2*TH3x1**2 - 6*complex(0,1)*lam3*TH3x1**4 - 12*alp1*complex(0,1)*TH1x1**2*TH4x1**2 - 12*alp2*complex(0,1)*TH1x1**2*TH4x1**2 - 12*complex(0,1)*lam4*TH3x1**2*TH4x1**2 - 6*complex(0,1)*lam3*TH4x1**4',
                  order = {'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x2 - 4*complex(0,1)*lam2*TH1x1*TH1x2 - 2*alp1*complex(0,1)*TH3x1*TH3x2 - 2*alp3*complex(0,1)*TH3x1*TH3x2 - 2*alp1*complex(0,1)*TH4x1*TH4x2 - 2*alp3*complex(0,1)*TH4x1*TH4x2',
                  order = {'QED':2})

GC_226 = Coupling(name = 'GC_226',
                  value = '(complex(0,1)*gR**2*TH1x1*TH1x2)/2. + (complex(0,1)*gR**2*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_227 = Coupling(name = 'GC_227',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x1*TH1x2)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x1*TH1x2 + (complex(0,1)*gL**2*sw**2*TH1x1*TH1x2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x1*TH3x2)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x1*TH3x2 + (complex(0,1)*gL**2*sw**2*TH3x1*TH3x2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x1*TH4x2)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x1*TH4x2 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_228 = Coupling(name = 'GC_228',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x1*TH1x2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x1*TH1x2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x1*TH1x2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x1*TH1x2)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x1*TH1x2)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x1*TH1x2)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x1*TH3x2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x1*TH3x2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x1*TH3x2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x1*TH3x2)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x1*TH3x2)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x1*TH3x2)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x1*TH4x2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x1*TH4x2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x1*TH4x2)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x1*TH4x2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x1*TH4x2)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x1*TH4x2 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_229 = Coupling(name = 'GC_229',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x1*TH1x2)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x1*TH1x2)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x1*TH1x2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x1*TH1x2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x1*TH1x2)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x1*TH1x2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x1*TH3x2)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x1*TH3x2)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x1*TH3x2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x1*TH3x2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x1*TH3x2)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x1*TH3x2)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x1*TH4x2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x1*TH4x2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x1*TH4x2)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x1*TH4x2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x1*TH4x2)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x1*TH4x2 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_230 = Coupling(name = 'GC_230',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x1*TH1x2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1*TH1x2 + (cph**2*complex(0,1)*gR**2*st**2*TH1x1*TH1x2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x1*TH1x2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1*TH1x2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x1*TH1x2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x1*TH3x2)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*TH3x2 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x1*TH3x2)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x1*TH3x2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*TH3x2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x1*TH3x2)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x1*TH4x2)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x1*TH4x2 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x1*TH4x2)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*TH4x2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*TH4x2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*TH4x2 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*TH4x2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x1*TH4x2)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x1*TH4x2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_231 = Coupling(name = 'GC_231',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x1*TH1x2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x1*TH1x2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x1*TH1x2)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x1*TH1x2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x1*TH1x2)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x1*TH1x2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x1*TH1x2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x1*TH1x2)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x1*TH3x2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x1*TH3x2)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x1*TH3x2)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x1*TH3x2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x1*TH3x2)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x1*TH3x2 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x1*TH3x2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x1*TH3x2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x1*TH4x2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x1*TH4x2 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x1*TH4x2)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x1*TH4x2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x1*TH4x2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x1*TH4x2)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x1*TH4x2)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x1*TH4x2)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x1*TH4x2)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x1*TH4x2)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x1*TH4x2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x1*TH4x2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x1*TH4x2 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_232 = Coupling(name = 'GC_232',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x1*TH1x2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1*TH1x2 + (cw**2*complex(0,1)*gL**2*st**2*TH1x1*TH1x2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1*TH1x2 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x1*TH1x2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x1*TH1x2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x1*TH3x2)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*TH3x2 + (cw**2*complex(0,1)*gL**2*st**2*TH3x1*TH3x2)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*TH3x2 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x1*TH3x2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x1*TH3x2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x1*TH4x2)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x1*TH4x2 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x1*TH4x2)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*TH4x2 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*TH4x2 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*TH4x2 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*TH4x2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x1*TH4x2)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x1*TH4x2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x1*TH4x2)/2.',
                  order = {'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '-6*complex(0,1)*lam1*TH1x1**3*TH1x2 - 6*alp1*complex(0,1)*TH1x1*TH1x2*TH3x1**2 - 6*alp2*complex(0,1)*TH1x1*TH1x2*TH3x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH3x1*TH3x2 - 6*alp2*complex(0,1)*TH1x1**2*TH3x1*TH3x2 - 6*complex(0,1)*lam3*TH3x1**3*TH3x2 - 6*alp1*complex(0,1)*TH1x1*TH1x2*TH4x1**2 - 6*alp2*complex(0,1)*TH1x1*TH1x2*TH4x1**2 - 6*complex(0,1)*lam4*TH3x1*TH3x2*TH4x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH4x1*TH4x2 - 6*alp2*complex(0,1)*TH1x1**2*TH4x1*TH4x2 - 6*complex(0,1)*lam4*TH3x1**2*TH4x1*TH4x2 - 6*complex(0,1)*lam3*TH4x1**3*TH4x2',
                  order = {'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = '-2*complex(0,1)*lam1 - 2*complex(0,1)*lam1*TH1x2**2 - 4*complex(0,1)*lam2*TH1x2**2 - 2*alp1*complex(0,1)*TH3x2**2 - 2*alp3*complex(0,1)*TH3x2**2 - 2*alp1*complex(0,1)*TH4x2**2 - 2*alp3*complex(0,1)*TH4x2**2',
                  order = {'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '(complex(0,1)*gR**2)/2. + (complex(0,1)*gR**2*TH1x2**2)/2. + (complex(0,1)*gR**2*TH4x2**2)/2.',
                  order = {'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2)/2. - cw*complex(0,1)*gL*gR*sph*sw + (complex(0,1)*gL**2*sw**2)/2. + (cw**2*complex(0,1)*gR**2*sph**2*TH1x2**2)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x2**2 + (complex(0,1)*gL**2*sw**2*TH1x2**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x2**2)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x2**2 + (complex(0,1)*gL**2*sw**2*TH3x2**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x2**2)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x2**2 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x2**2)/2.',
                  order = {'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph)/2. + (cph*cw*complex(0,1)*gR**2*sph*st)/2. + (ct*cw*complex(0,1)*gL**2*sw)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw)/2. - (cph*complex(0,1)*gL*gR*st*sw)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2)/2. - (ct*cw**2*complex(0,1)*gL*gR*sph*TH1x2**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x2**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x2**2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x2**2)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x2**2)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x2**2)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x2**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x2**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x2**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x2**2)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x2**2)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x2**2)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x2**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x2**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x2**2)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x2**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x2**2)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x2**2 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x2**2)/2.',
                  order = {'QED':2})

GC_238 = Coupling(name = 'GC_238',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph)/2. + (cw**2*complex(0,1)*gL*gR*sph*st)/2. - (cph*ct*complex(0,1)*gL*gR*sw)/2. - (cw*complex(0,1)*gL**2*st*sw)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw)/2. - (complex(0,1)*gL*gR*sph*st*sw**2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH1x2**2)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x2**2)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x2**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x2**2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x2**2)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x2**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x2**2)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x2**2)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x2**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x2**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x2**2)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x2**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x2**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x2**2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x2**2)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x2**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x2**2)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x2**2 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x2**2)/2.',
                  order = {'QED':2})

GC_239 = Coupling(name = 'GC_239',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st + (cph**2*complex(0,1)*gR**2*st**2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw - cph*ct*complex(0,1)*gR**2*sph*st*sw + (ct**2*complex(0,1)*gR**2*sph**2*sw**2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH1x2**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x2**2 + (cph**2*complex(0,1)*gR**2*st**2*TH1x2**2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x2**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x2**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x2**2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x2**2)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x2**2)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x2**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x2**2)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x2**2)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x2**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x2**2)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2**2 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x2**2)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x2**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x2**2)/2.',
                  order = {'QED':2})

GC_240 = Coupling(name = 'GC_240',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR)/2. - (ct*cw**2*complex(0,1)*gL**2*st)/2. + (cph**2*ct*complex(0,1)*gR**2*st)/2. + (cph*cw*complex(0,1)*gL*gR*st**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw + (cph*complex(0,1)*gR**2*sph*st**2*sw)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2)/2. - (cph*ct**2*cw*complex(0,1)*gL*gR*TH1x2**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x2**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x2**2)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x2**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x2**2)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x2**2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x2**2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x2**2)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x2**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x2**2)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x2**2)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x2**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x2**2)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x2**2 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x2**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x2**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x2**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x2**2 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x2**2)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x2**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x2**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x2**2)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x2**2)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x2**2)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x2**2)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x2**2)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x2**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x2**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x2**2 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x2**2)/2.',
                  order = {'QED':2})

GC_241 = Coupling(name = 'GC_241',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st + (cw**2*complex(0,1)*gL**2*st**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw + cw*complex(0,1)*gL*gR*sph*st**2*sw + (complex(0,1)*gR**2*sph**2*st**2*sw**2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH1x2**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x2**2 + (cw**2*complex(0,1)*gL**2*st**2*TH1x2**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x2**2 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x2**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x2**2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x2**2)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2**2 + (cw**2*complex(0,1)*gL**2*st**2*TH3x2**2)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2**2 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x2**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x2**2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x2**2)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x2**2 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x2**2)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2**2 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2**2 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2**2 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x2**2)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x2**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x2**2)/2.',
                  order = {'QED':2})

GC_242 = Coupling(name = 'GC_242',
                  value = '-2*complex(0,1)*lam1*TH1x1**2 - 4*complex(0,1)*lam2*TH1x1**2 - 6*complex(0,1)*lam1*TH1x1**2*TH1x2**2 - 2*alp1*complex(0,1)*TH3x1**2 - 2*alp3*complex(0,1)*TH3x1**2 - 2*alp1*complex(0,1)*TH1x2**2*TH3x1**2 - 2*alp2*complex(0,1)*TH1x2**2*TH3x1**2 - 8*alp1*complex(0,1)*TH1x1*TH1x2*TH3x1*TH3x2 - 8*alp2*complex(0,1)*TH1x1*TH1x2*TH3x1*TH3x2 - 2*alp1*complex(0,1)*TH1x1**2*TH3x2**2 - 2*alp2*complex(0,1)*TH1x1**2*TH3x2**2 - 6*complex(0,1)*lam3*TH3x1**2*TH3x2**2 - 2*alp1*complex(0,1)*TH4x1**2 - 2*alp3*complex(0,1)*TH4x1**2 - 2*alp1*complex(0,1)*TH1x2**2*TH4x1**2 - 2*alp2*complex(0,1)*TH1x2**2*TH4x1**2 - 2*complex(0,1)*lam4*TH3x2**2*TH4x1**2 - 8*alp1*complex(0,1)*TH1x1*TH1x2*TH4x1*TH4x2 - 8*alp2*complex(0,1)*TH1x1*TH1x2*TH4x1*TH4x2 - 8*complex(0,1)*lam4*TH3x1*TH3x2*TH4x1*TH4x2 - 2*alp1*complex(0,1)*TH1x1**2*TH4x2**2 - 2*alp2*complex(0,1)*TH1x1**2*TH4x2**2 - 2*complex(0,1)*lam4*TH3x1**2*TH4x2**2 - 6*complex(0,1)*lam3*TH4x1**2*TH4x2**2',
                  order = {'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x2 - 4*complex(0,1)*lam2*TH1x1*TH1x2 - 6*complex(0,1)*lam1*TH1x1*TH1x2**3 - 2*alp1*complex(0,1)*TH3x1*TH3x2 - 2*alp3*complex(0,1)*TH3x1*TH3x2 - 6*alp1*complex(0,1)*TH1x2**2*TH3x1*TH3x2 - 6*alp2*complex(0,1)*TH1x2**2*TH3x1*TH3x2 - 6*alp1*complex(0,1)*TH1x1*TH1x2*TH3x2**2 - 6*alp2*complex(0,1)*TH1x1*TH1x2*TH3x2**2 - 6*complex(0,1)*lam3*TH3x1*TH3x2**3 - 2*alp1*complex(0,1)*TH4x1*TH4x2 - 2*alp3*complex(0,1)*TH4x1*TH4x2 - 6*alp1*complex(0,1)*TH1x2**2*TH4x1*TH4x2 - 6*alp2*complex(0,1)*TH1x2**2*TH4x1*TH4x2 - 6*complex(0,1)*lam4*TH3x2**2*TH4x1*TH4x2 - 6*alp1*complex(0,1)*TH1x1*TH1x2*TH4x2**2 - 6*alp2*complex(0,1)*TH1x1*TH1x2*TH4x2**2 - 6*complex(0,1)*lam4*TH3x1*TH3x2*TH4x2**2 - 6*complex(0,1)*lam3*TH4x1*TH4x2**3',
                  order = {'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '-6*complex(0,1)*lam1 - 2*complex(0,1)*lam1*TH1x2**2 - 4*complex(0,1)*lam2*TH1x2**2 - 6*complex(0,1)*lam1*TH1x2**4 - 2*alp1*complex(0,1)*TH3x2**2 - 2*alp3*complex(0,1)*TH3x2**2 - 12*alp1*complex(0,1)*TH1x2**2*TH3x2**2 - 12*alp2*complex(0,1)*TH1x2**2*TH3x2**2 - 6*complex(0,1)*lam3*TH3x2**4 - 2*alp1*complex(0,1)*TH4x2**2 - 2*alp3*complex(0,1)*TH4x2**2 - 12*alp1*complex(0,1)*TH1x2**2*TH4x2**2 - 12*alp2*complex(0,1)*TH1x2**2*TH4x2**2 - 12*complex(0,1)*lam4*TH3x2**2*TH4x2**2 - 6*complex(0,1)*lam3*TH4x2**4',
                  order = {'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x3 - 4*complex(0,1)*lam2*TH1x1*TH1x3 - 2*alp1*complex(0,1)*TH3x1*TH3x3 - 2*alp3*complex(0,1)*TH3x1*TH3x3 - 2*alp1*complex(0,1)*TH4x1*TH4x3 - 2*alp3*complex(0,1)*TH4x1*TH4x3',
                  order = {'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '(complex(0,1)*gR**2*TH1x1*TH1x3)/2. + (complex(0,1)*gR**2*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x1*TH1x3)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x1*TH1x3 + (complex(0,1)*gL**2*sw**2*TH1x1*TH1x3)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x1*TH3x3)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x1*TH3x3 + (complex(0,1)*gL**2*sw**2*TH3x1*TH3x3)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x1*TH4x3)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x1*TH4x3 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x1*TH1x3)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x1*TH1x3)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x1*TH1x3)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x1*TH1x3)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x1*TH1x3)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x1*TH1x3)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x1*TH3x3)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x1*TH3x3)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x1*TH3x3)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x1*TH3x3)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x1*TH3x3)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x1*TH3x3)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x1*TH4x3)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x1*TH4x3)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x1*TH4x3)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x1*TH4x3)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x1*TH4x3)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x1*TH4x3 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x1*TH1x3)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x1*TH1x3)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x1*TH1x3)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x1*TH1x3)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x1*TH1x3)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x1*TH1x3)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x1*TH3x3)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x1*TH3x3)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x1*TH3x3)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x1*TH3x3)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x1*TH3x3)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x1*TH3x3)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x1*TH4x3)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x1*TH4x3)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x1*TH4x3)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x1*TH4x3)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x1*TH4x3)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x1*TH4x3 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x1*TH1x3)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1*TH1x3 + (cph**2*complex(0,1)*gR**2*st**2*TH1x1*TH1x3)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x1*TH1x3 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1*TH1x3 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x1*TH1x3)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x1*TH3x3)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*TH3x3 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x1*TH3x3)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x1*TH3x3 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*TH3x3 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x1*TH3x3)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x1*TH4x3)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x1*TH4x3 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x1*TH4x3)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*TH4x3 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*TH4x3 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*TH4x3 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*TH4x3 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x1*TH4x3)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x1*TH4x3 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x1*TH1x3)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x1*TH1x3)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x1*TH1x3)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x1*TH1x3)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x1*TH1x3)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x1*TH1x3 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x1*TH1x3)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x1*TH1x3)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x1*TH3x3)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x1*TH3x3)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x1*TH3x3)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x1*TH3x3)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x1*TH3x3)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x1*TH3x3 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x1*TH3x3)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x1*TH3x3)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x1*TH4x3)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x1*TH4x3 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x1*TH4x3)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x1*TH4x3)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x1*TH4x3)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x1*TH4x3)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x1*TH4x3)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x1*TH4x3)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x1*TH4x3)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x1*TH4x3)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x1*TH4x3)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x1*TH4x3)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x1*TH4x3 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x1*TH1x3)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1*TH1x3 + (cw**2*complex(0,1)*gL**2*st**2*TH1x1*TH1x3)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1*TH1x3 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x1*TH1x3 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x1*TH1x3)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x1*TH3x3)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*TH3x3 + (cw**2*complex(0,1)*gL**2*st**2*TH3x1*TH3x3)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*TH3x3 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x1*TH3x3 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x1*TH3x3)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x1*TH4x3)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x1*TH4x3 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x1*TH4x3)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*TH4x3 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*TH4x3 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*TH4x3 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*TH4x3 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x1*TH4x3)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x1*TH4x3 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x1*TH4x3)/2.',
                  order = {'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '-6*complex(0,1)*lam1*TH1x1**3*TH1x3 - 6*alp1*complex(0,1)*TH1x1*TH1x3*TH3x1**2 - 6*alp2*complex(0,1)*TH1x1*TH1x3*TH3x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH3x1*TH3x3 - 6*alp2*complex(0,1)*TH1x1**2*TH3x1*TH3x3 - 6*complex(0,1)*lam3*TH3x1**3*TH3x3 - 6*alp1*complex(0,1)*TH1x1*TH1x3*TH4x1**2 - 6*alp2*complex(0,1)*TH1x1*TH1x3*TH4x1**2 - 6*complex(0,1)*lam4*TH3x1*TH3x3*TH4x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH4x1*TH4x3 - 6*alp2*complex(0,1)*TH1x1**2*TH4x1*TH4x3 - 6*complex(0,1)*lam4*TH3x1**2*TH4x1*TH4x3 - 6*complex(0,1)*lam3*TH4x1**3*TH4x3',
                  order = {'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x3 - 4*complex(0,1)*lam2*TH1x2*TH1x3 - 2*alp1*complex(0,1)*TH3x2*TH3x3 - 2*alp3*complex(0,1)*TH3x2*TH3x3 - 2*alp1*complex(0,1)*TH4x2*TH4x3 - 2*alp3*complex(0,1)*TH4x2*TH4x3',
                  order = {'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(complex(0,1)*gR**2*TH1x2*TH1x3)/2. + (complex(0,1)*gR**2*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x2*TH1x3)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x2*TH1x3 + (complex(0,1)*gL**2*sw**2*TH1x2*TH1x3)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x2*TH3x3)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x2*TH3x3 + (complex(0,1)*gL**2*sw**2*TH3x2*TH3x3)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x2*TH4x3)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x2*TH4x3 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x2*TH1x3)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x2*TH1x3)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x2*TH1x3)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x2*TH1x3)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x2*TH1x3)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x2*TH1x3)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x2*TH3x3)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x2*TH3x3)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x2*TH3x3)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x2*TH3x3)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x2*TH3x3)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x2*TH3x3)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x2*TH4x3)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x2*TH4x3)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x2*TH4x3)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x2*TH4x3)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x2*TH4x3)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x2*TH4x3 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x2*TH1x3)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x2*TH1x3)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x2*TH1x3)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x2*TH1x3)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x2*TH1x3)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x2*TH1x3)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x2*TH3x3)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x2*TH3x3)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x2*TH3x3)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x2*TH3x3)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x2*TH3x3)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x2*TH3x3)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x2*TH4x3)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x2*TH4x3)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x2*TH4x3)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x2*TH4x3)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x2*TH4x3)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x2*TH4x3 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x2*TH1x3)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x2*TH1x3 + (cph**2*complex(0,1)*gR**2*st**2*TH1x2*TH1x3)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x2*TH1x3 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x2*TH1x3 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x2*TH1x3)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x2*TH3x3)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2*TH3x3 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x2*TH3x3)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x2*TH3x3 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2*TH3x3 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x2*TH3x3)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x2*TH4x3)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x2*TH4x3 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x2*TH4x3)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2*TH4x3 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2*TH4x3 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2*TH4x3 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2*TH4x3 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x2*TH4x3)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x2*TH4x3 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x2*TH1x3)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x2*TH1x3)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x2*TH1x3)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x2*TH1x3)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x2*TH1x3)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x2*TH1x3 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x2*TH1x3)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x2*TH1x3)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x2*TH3x3)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x2*TH3x3)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x2*TH3x3)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x2*TH3x3)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x2*TH3x3)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x2*TH3x3 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x2*TH3x3)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x2*TH3x3)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x2*TH4x3)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x2*TH4x3 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x2*TH4x3)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x2*TH4x3)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x2*TH4x3)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x2*TH4x3)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x2*TH4x3)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x2*TH4x3)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x2*TH4x3)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x2*TH4x3)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x2*TH4x3)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x2*TH4x3)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x2*TH4x3 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x2*TH1x3)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x2*TH1x3 + (cw**2*complex(0,1)*gL**2*st**2*TH1x2*TH1x3)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x2*TH1x3 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x2*TH1x3 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x2*TH1x3)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x2*TH3x3)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2*TH3x3 + (cw**2*complex(0,1)*gL**2*st**2*TH3x2*TH3x3)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2*TH3x3 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x2*TH3x3 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x2*TH3x3)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x2*TH4x3)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x2*TH4x3 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x2*TH4x3)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2*TH4x3 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2*TH4x3 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2*TH4x3 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2*TH4x3 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x2*TH4x3)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x2*TH4x3 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x2*TH4x3)/2.',
                  order = {'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '-6*complex(0,1)*lam1*TH1x1**2*TH1x2*TH1x3 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH3x1**2 - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH3x1**2 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH3x1*TH3x2 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH3x1*TH3x2 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH3x1*TH3x3 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH3x1*TH3x3 - 2*alp1*complex(0,1)*TH1x1**2*TH3x2*TH3x3 - 2*alp2*complex(0,1)*TH1x1**2*TH3x2*TH3x3 - 6*complex(0,1)*lam3*TH3x1**2*TH3x2*TH3x3 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH4x1**2 - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH4x1**2 - 2*complex(0,1)*lam4*TH3x2*TH3x3*TH4x1**2 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH4x1*TH4x2 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH4x1*TH4x2 - 4*complex(0,1)*lam4*TH3x1*TH3x3*TH4x1*TH4x2 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH4x1*TH4x3 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH4x1*TH4x3 - 4*complex(0,1)*lam4*TH3x1*TH3x2*TH4x1*TH4x3 - 2*alp1*complex(0,1)*TH1x1**2*TH4x2*TH4x3 - 2*alp2*complex(0,1)*TH1x1**2*TH4x2*TH4x3 - 2*complex(0,1)*lam4*TH3x1**2*TH4x2*TH4x3 - 6*complex(0,1)*lam3*TH4x1**2*TH4x2*TH4x3',
                  order = {'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x3 - 4*complex(0,1)*lam2*TH1x1*TH1x3 - 6*complex(0,1)*lam1*TH1x1*TH1x2**2*TH1x3 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH3x1*TH3x2 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH3x1*TH3x2 - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH3x2**2 - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH3x2**2 - 2*alp1*complex(0,1)*TH3x1*TH3x3 - 2*alp3*complex(0,1)*TH3x1*TH3x3 - 2*alp1*complex(0,1)*TH1x2**2*TH3x1*TH3x3 - 2*alp2*complex(0,1)*TH1x2**2*TH3x1*TH3x3 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH3x2*TH3x3 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH3x2*TH3x3 - 6*complex(0,1)*lam3*TH3x1*TH3x2**2*TH3x3 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH4x1*TH4x2 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH4x1*TH4x2 - 4*complex(0,1)*lam4*TH3x2*TH3x3*TH4x1*TH4x2 - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH4x2**2 - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH4x2**2 - 2*complex(0,1)*lam4*TH3x1*TH3x3*TH4x2**2 - 2*alp1*complex(0,1)*TH4x1*TH4x3 - 2*alp3*complex(0,1)*TH4x1*TH4x3 - 2*alp1*complex(0,1)*TH1x2**2*TH4x1*TH4x3 - 2*alp2*complex(0,1)*TH1x2**2*TH4x1*TH4x3 - 2*complex(0,1)*lam4*TH3x2**2*TH4x1*TH4x3 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH4x2*TH4x3 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH4x2*TH4x3 - 4*complex(0,1)*lam4*TH3x1*TH3x2*TH4x2*TH4x3 - 6*complex(0,1)*lam3*TH4x1*TH4x2**2*TH4x3',
                  order = {'QED':2})

GC_264 = Coupling(name = 'GC_264',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x3 - 4*complex(0,1)*lam2*TH1x2*TH1x3 - 6*complex(0,1)*lam1*TH1x2**3*TH1x3 - 6*alp1*complex(0,1)*TH1x2*TH1x3*TH3x2**2 - 6*alp2*complex(0,1)*TH1x2*TH1x3*TH3x2**2 - 2*alp1*complex(0,1)*TH3x2*TH3x3 - 2*alp3*complex(0,1)*TH3x2*TH3x3 - 6*alp1*complex(0,1)*TH1x2**2*TH3x2*TH3x3 - 6*alp2*complex(0,1)*TH1x2**2*TH3x2*TH3x3 - 6*complex(0,1)*lam3*TH3x2**3*TH3x3 - 6*alp1*complex(0,1)*TH1x2*TH1x3*TH4x2**2 - 6*alp2*complex(0,1)*TH1x2*TH1x3*TH4x2**2 - 6*complex(0,1)*lam4*TH3x2*TH3x3*TH4x2**2 - 2*alp1*complex(0,1)*TH4x2*TH4x3 - 2*alp3*complex(0,1)*TH4x2*TH4x3 - 6*alp1*complex(0,1)*TH1x2**2*TH4x2*TH4x3 - 6*alp2*complex(0,1)*TH1x2**2*TH4x2*TH4x3 - 6*complex(0,1)*lam4*TH3x2**2*TH4x2*TH4x3 - 6*complex(0,1)*lam3*TH4x2**3*TH4x3',
                  order = {'QED':2})

GC_265 = Coupling(name = 'GC_265',
                  value = '-2*complex(0,1)*lam1*TH1x3**2 - 4*complex(0,1)*lam2*TH1x3**2 - 2*alp1*complex(0,1)*TH3x3**2 - 2*alp3*complex(0,1)*TH3x3**2 - 2*alp1*complex(0,1)*TH4x3**2 - 2*alp3*complex(0,1)*TH4x3**2',
                  order = {'QED':2})

GC_266 = Coupling(name = 'GC_266',
                  value = '(complex(0,1)*gR**2*TH1x3**2)/2. + (complex(0,1)*gR**2*TH4x3**2)/2.',
                  order = {'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x3**2)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x3**2 + (complex(0,1)*gL**2*sw**2*TH1x3**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x3**2)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x3**2 + (complex(0,1)*gL**2*sw**2*TH3x3**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x3**2)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x3**2 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x3**2)/2.',
                  order = {'QED':2})

GC_268 = Coupling(name = 'GC_268',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x3**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x3**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x3**2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x3**2)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x3**2)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x3**2)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x3**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x3**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x3**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x3**2)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x3**2)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x3**2)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x3**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x3**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x3**2)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x3**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x3**2)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x3**2 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x3**2)/2.',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x3**2)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x3**2)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x3**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x3**2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x3**2)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x3**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x3**2)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x3**2)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x3**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x3**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x3**2)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x3**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x3**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x3**2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x3**2)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x3**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x3**2)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x3**2 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x3**2)/2.',
                  order = {'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x3**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x3**2 + (cph**2*complex(0,1)*gR**2*st**2*TH1x3**2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x3**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x3**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x3**2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x3**2)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x3**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x3**2)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x3**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x3**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x3**2)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x3**2)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x3**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x3**2)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x3**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x3**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x3**2 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x3**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x3**2)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x3**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x3**2)/2.',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x3**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x3**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x3**2)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x3**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x3**2)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x3**2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x3**2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x3**2)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x3**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x3**2)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x3**2)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x3**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x3**2)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x3**2 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x3**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x3**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x3**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x3**2 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x3**2)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x3**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x3**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x3**2)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x3**2)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x3**2)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x3**2)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x3**2)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x3**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x3**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x3**2 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x3**2)/2.',
                  order = {'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x3**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x3**2 + (cw**2*complex(0,1)*gL**2*st**2*TH1x3**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x3**2 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x3**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x3**2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x3**2)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x3**2 + (cw**2*complex(0,1)*gL**2*st**2*TH3x3**2)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x3**2 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x3**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x3**2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x3**2)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x3**2 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x3**2)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x3**2 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x3**2 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x3**2 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x3**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x3**2)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x3**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x3**2)/2.',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '-6*complex(0,1)*lam1*TH1x1**2*TH1x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x1**2 - 2*alp2*complex(0,1)*TH1x3**2*TH3x1**2 - 8*alp1*complex(0,1)*TH1x1*TH1x3*TH3x1*TH3x3 - 8*alp2*complex(0,1)*TH1x1*TH1x3*TH3x1*TH3x3 - 2*alp1*complex(0,1)*TH1x1**2*TH3x3**2 - 2*alp2*complex(0,1)*TH1x1**2*TH3x3**2 - 6*complex(0,1)*lam3*TH3x1**2*TH3x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH4x1**2 - 2*alp2*complex(0,1)*TH1x3**2*TH4x1**2 - 2*complex(0,1)*lam4*TH3x3**2*TH4x1**2 - 8*alp1*complex(0,1)*TH1x1*TH1x3*TH4x1*TH4x3 - 8*alp2*complex(0,1)*TH1x1*TH1x3*TH4x1*TH4x3 - 8*complex(0,1)*lam4*TH3x1*TH3x3*TH4x1*TH4x3 - 2*alp1*complex(0,1)*TH1x1**2*TH4x3**2 - 2*alp2*complex(0,1)*TH1x1**2*TH4x3**2 - 2*complex(0,1)*lam4*TH3x1**2*TH4x3**2 - 6*complex(0,1)*lam3*TH4x1**2*TH4x3**2',
                  order = {'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x2*TH1x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x1*TH3x2 - 2*alp2*complex(0,1)*TH1x3**2*TH3x1*TH3x2 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH3x1*TH3x3 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH3x1*TH3x3 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH3x2*TH3x3 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH3x2*TH3x3 - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH3x3**2 - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH3x3**2 - 6*complex(0,1)*lam3*TH3x1*TH3x2*TH3x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH4x1*TH4x2 - 2*alp2*complex(0,1)*TH1x3**2*TH4x1*TH4x2 - 2*complex(0,1)*lam4*TH3x3**2*TH4x1*TH4x2 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH4x1*TH4x3 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH4x1*TH4x3 - 4*complex(0,1)*lam4*TH3x2*TH3x3*TH4x1*TH4x3 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH4x2*TH4x3 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH4x2*TH4x3 - 4*complex(0,1)*lam4*TH3x1*TH3x3*TH4x2*TH4x3 - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH4x3**2 - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH4x3**2 - 2*complex(0,1)*lam4*TH3x1*TH3x2*TH4x3**2 - 6*complex(0,1)*lam3*TH4x1*TH4x2*TH4x3**2',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '-2*complex(0,1)*lam1*TH1x3**2 - 4*complex(0,1)*lam2*TH1x3**2 - 6*complex(0,1)*lam1*TH1x2**2*TH1x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x2**2 - 2*alp2*complex(0,1)*TH1x3**2*TH3x2**2 - 8*alp1*complex(0,1)*TH1x2*TH1x3*TH3x2*TH3x3 - 8*alp2*complex(0,1)*TH1x2*TH1x3*TH3x2*TH3x3 - 2*alp1*complex(0,1)*TH3x3**2 - 2*alp3*complex(0,1)*TH3x3**2 - 2*alp1*complex(0,1)*TH1x2**2*TH3x3**2 - 2*alp2*complex(0,1)*TH1x2**2*TH3x3**2 - 6*complex(0,1)*lam3*TH3x2**2*TH3x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH4x2**2 - 2*alp2*complex(0,1)*TH1x3**2*TH4x2**2 - 2*complex(0,1)*lam4*TH3x3**2*TH4x2**2 - 8*alp1*complex(0,1)*TH1x2*TH1x3*TH4x2*TH4x3 - 8*alp2*complex(0,1)*TH1x2*TH1x3*TH4x2*TH4x3 - 8*complex(0,1)*lam4*TH3x2*TH3x3*TH4x2*TH4x3 - 2*alp1*complex(0,1)*TH4x3**2 - 2*alp3*complex(0,1)*TH4x3**2 - 2*alp1*complex(0,1)*TH1x2**2*TH4x3**2 - 2*alp2*complex(0,1)*TH1x2**2*TH4x3**2 - 2*complex(0,1)*lam4*TH3x2**2*TH4x3**2 - 6*complex(0,1)*lam3*TH4x2**2*TH4x3**2',
                  order = {'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x3**3 - 6*alp1*complex(0,1)*TH1x3**2*TH3x1*TH3x3 - 6*alp2*complex(0,1)*TH1x3**2*TH3x1*TH3x3 - 6*alp1*complex(0,1)*TH1x1*TH1x3*TH3x3**2 - 6*alp2*complex(0,1)*TH1x1*TH1x3*TH3x3**2 - 6*complex(0,1)*lam3*TH3x1*TH3x3**3 - 6*alp1*complex(0,1)*TH1x3**2*TH4x1*TH4x3 - 6*alp2*complex(0,1)*TH1x3**2*TH4x1*TH4x3 - 6*complex(0,1)*lam4*TH3x3**2*TH4x1*TH4x3 - 6*alp1*complex(0,1)*TH1x1*TH1x3*TH4x3**2 - 6*alp2*complex(0,1)*TH1x1*TH1x3*TH4x3**2 - 6*complex(0,1)*lam4*TH3x1*TH3x3*TH4x3**2 - 6*complex(0,1)*lam3*TH4x1*TH4x3**3',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '-6*complex(0,1)*lam1*TH1x2*TH1x3**3 - 6*alp1*complex(0,1)*TH1x3**2*TH3x2*TH3x3 - 6*alp2*complex(0,1)*TH1x3**2*TH3x2*TH3x3 - 6*alp1*complex(0,1)*TH1x2*TH1x3*TH3x3**2 - 6*alp2*complex(0,1)*TH1x2*TH1x3*TH3x3**2 - 6*complex(0,1)*lam3*TH3x2*TH3x3**3 - 6*alp1*complex(0,1)*TH1x3**2*TH4x2*TH4x3 - 6*alp2*complex(0,1)*TH1x3**2*TH4x2*TH4x3 - 6*complex(0,1)*lam4*TH3x3**2*TH4x2*TH4x3 - 6*alp1*complex(0,1)*TH1x2*TH1x3*TH4x3**2 - 6*alp2*complex(0,1)*TH1x2*TH1x3*TH4x3**2 - 6*complex(0,1)*lam4*TH3x2*TH3x3*TH4x3**2 - 6*complex(0,1)*lam3*TH4x2*TH4x3**3',
                  order = {'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '-6*complex(0,1)*lam1*TH1x3**4 - 12*alp1*complex(0,1)*TH1x3**2*TH3x3**2 - 12*alp2*complex(0,1)*TH1x3**2*TH3x3**2 - 6*complex(0,1)*lam3*TH3x3**4 - 12*alp1*complex(0,1)*TH1x3**2*TH4x3**2 - 12*alp2*complex(0,1)*TH1x3**2*TH4x3**2 - 12*complex(0,1)*lam4*TH3x3**2*TH4x3**2 - 6*complex(0,1)*lam3*TH4x3**4',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x4 - 4*complex(0,1)*lam2*TH1x1*TH1x4 - 2*alp1*complex(0,1)*TH3x1*TH3x4 - 2*alp3*complex(0,1)*TH3x1*TH3x4 - 2*alp1*complex(0,1)*TH4x1*TH4x4 - 2*alp3*complex(0,1)*TH4x1*TH4x4',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '(complex(0,1)*gR**2*TH1x1*TH1x4)/2. + (complex(0,1)*gR**2*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x1*TH1x4)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x1*TH1x4 + (complex(0,1)*gL**2*sw**2*TH1x1*TH1x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x1*TH3x4)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x1*TH3x4 + (complex(0,1)*gL**2*sw**2*TH3x1*TH3x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x1*TH4x4)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x1*TH4x4 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x1*TH1x4)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x1*TH1x4)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x1*TH1x4)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x1*TH1x4)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x1*TH1x4)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x1*TH1x4)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x1*TH3x4)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x1*TH3x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x1*TH3x4)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x1*TH3x4)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x1*TH3x4)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x1*TH3x4)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x1*TH4x4)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x1*TH4x4)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x1*TH4x4)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x1*TH4x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x1*TH4x4)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x1*TH4x4 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x1*TH1x4)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x1*TH1x4)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x1*TH1x4)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x1*TH1x4)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x1*TH1x4)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x1*TH1x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x1*TH3x4)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x1*TH3x4)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x1*TH3x4)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x1*TH3x4)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x1*TH3x4)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x1*TH3x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x1*TH4x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x1*TH4x4)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x1*TH4x4)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x1*TH4x4)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x1*TH4x4)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x1*TH4x4 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x1*TH1x4)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1*TH1x4 + (cph**2*complex(0,1)*gR**2*st**2*TH1x1*TH1x4)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x1*TH1x4 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1*TH1x4 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x1*TH1x4)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x1*TH3x4)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*TH3x4 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x1*TH3x4)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x1*TH3x4 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*TH3x4 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x1*TH3x4)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x1*TH4x4)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x1*TH4x4 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x1*TH4x4)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*TH4x4 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*TH4x4 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*TH4x4 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*TH4x4 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x1*TH4x4)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x1*TH4x4 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x1*TH1x4)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x1*TH1x4)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x1*TH1x4)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x1*TH1x4)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x1*TH1x4)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x1*TH1x4 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x1*TH1x4)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x1*TH1x4)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x1*TH3x4)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x1*TH3x4)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x1*TH3x4)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x1*TH3x4)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x1*TH3x4)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x1*TH3x4 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x1*TH3x4)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x1*TH3x4)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x1*TH4x4)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x1*TH4x4 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x1*TH4x4)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x1*TH4x4)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x1*TH4x4)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x1*TH4x4)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x1*TH4x4)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x1*TH4x4)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x1*TH4x4)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x1*TH4x4)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x1*TH4x4)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x1*TH4x4)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x1*TH4x4 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x1*TH1x4)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x1*TH1x4 + (cw**2*complex(0,1)*gL**2*st**2*TH1x1*TH1x4)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x1*TH1x4 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x1*TH1x4 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x1*TH1x4)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x1*TH3x4)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*TH3x4 + (cw**2*complex(0,1)*gL**2*st**2*TH3x1*TH3x4)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*TH3x4 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x1*TH3x4 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x1*TH3x4)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x1*TH4x4)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x1*TH4x4 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x1*TH4x4)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*TH4x4 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*TH4x4 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*TH4x4 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*TH4x4 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x1*TH4x4)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x1*TH4x4 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x1*TH4x4)/2.',
                  order = {'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '-6*complex(0,1)*lam1*TH1x1**3*TH1x4 - 6*alp1*complex(0,1)*TH1x1*TH1x4*TH3x1**2 - 6*alp2*complex(0,1)*TH1x1*TH1x4*TH3x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH3x1*TH3x4 - 6*alp2*complex(0,1)*TH1x1**2*TH3x1*TH3x4 - 6*complex(0,1)*lam3*TH3x1**3*TH3x4 - 6*alp1*complex(0,1)*TH1x1*TH1x4*TH4x1**2 - 6*alp2*complex(0,1)*TH1x1*TH1x4*TH4x1**2 - 6*complex(0,1)*lam4*TH3x1*TH3x4*TH4x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH4x1*TH4x4 - 6*alp2*complex(0,1)*TH1x1**2*TH4x1*TH4x4 - 6*complex(0,1)*lam4*TH3x1**2*TH4x1*TH4x4 - 6*complex(0,1)*lam3*TH4x1**3*TH4x4',
                  order = {'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x4 - 4*complex(0,1)*lam2*TH1x2*TH1x4 - 2*alp1*complex(0,1)*TH3x2*TH3x4 - 2*alp3*complex(0,1)*TH3x2*TH3x4 - 2*alp1*complex(0,1)*TH4x2*TH4x4 - 2*alp3*complex(0,1)*TH4x2*TH4x4',
                  order = {'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(complex(0,1)*gR**2*TH1x2*TH1x4)/2. + (complex(0,1)*gR**2*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x2*TH1x4)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x2*TH1x4 + (complex(0,1)*gL**2*sw**2*TH1x2*TH1x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x2*TH3x4)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x2*TH3x4 + (complex(0,1)*gL**2*sw**2*TH3x2*TH3x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x2*TH4x4)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x2*TH4x4 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x2*TH1x4)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x2*TH1x4)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x2*TH1x4)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x2*TH1x4)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x2*TH1x4)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x2*TH1x4)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x2*TH3x4)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x2*TH3x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x2*TH3x4)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x2*TH3x4)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x2*TH3x4)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x2*TH3x4)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x2*TH4x4)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x2*TH4x4)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x2*TH4x4)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x2*TH4x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x2*TH4x4)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x2*TH4x4 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x2*TH1x4)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x2*TH1x4)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x2*TH1x4)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x2*TH1x4)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x2*TH1x4)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x2*TH1x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x2*TH3x4)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x2*TH3x4)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x2*TH3x4)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x2*TH3x4)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x2*TH3x4)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x2*TH3x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x2*TH4x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x2*TH4x4)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x2*TH4x4)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x2*TH4x4)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x2*TH4x4)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x2*TH4x4 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x2*TH1x4)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x2*TH1x4 + (cph**2*complex(0,1)*gR**2*st**2*TH1x2*TH1x4)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x2*TH1x4 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x2*TH1x4 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x2*TH1x4)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x2*TH3x4)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2*TH3x4 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x2*TH3x4)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x2*TH3x4 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2*TH3x4 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x2*TH3x4)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x2*TH4x4)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x2*TH4x4 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x2*TH4x4)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2*TH4x4 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2*TH4x4 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2*TH4x4 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2*TH4x4 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x2*TH4x4)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x2*TH4x4 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x2*TH1x4)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x2*TH1x4)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x2*TH1x4)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x2*TH1x4)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x2*TH1x4)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x2*TH1x4 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x2*TH1x4)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x2*TH1x4)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x2*TH3x4)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x2*TH3x4)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x2*TH3x4)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x2*TH3x4)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x2*TH3x4)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x2*TH3x4 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x2*TH3x4)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x2*TH3x4)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x2*TH4x4)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x2*TH4x4 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x2*TH4x4)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x2*TH4x4)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x2*TH4x4)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x2*TH4x4)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x2*TH4x4)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x2*TH4x4)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x2*TH4x4)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x2*TH4x4)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x2*TH4x4)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x2*TH4x4)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x2*TH4x4 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x2*TH1x4)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x2*TH1x4 + (cw**2*complex(0,1)*gL**2*st**2*TH1x2*TH1x4)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x2*TH1x4 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x2*TH1x4 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x2*TH1x4)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x2*TH3x4)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2*TH3x4 + (cw**2*complex(0,1)*gL**2*st**2*TH3x2*TH3x4)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2*TH3x4 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x2*TH3x4 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x2*TH3x4)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x2*TH4x4)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x2*TH4x4 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x2*TH4x4)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2*TH4x4 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2*TH4x4 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2*TH4x4 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2*TH4x4 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x2*TH4x4)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x2*TH4x4 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x2*TH4x4)/2.',
                  order = {'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '-6*complex(0,1)*lam1*TH1x1**2*TH1x2*TH1x4 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH3x1**2 - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH3x1**2 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH3x1*TH3x2 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH3x1*TH3x2 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH3x1*TH3x4 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH3x1*TH3x4 - 2*alp1*complex(0,1)*TH1x1**2*TH3x2*TH3x4 - 2*alp2*complex(0,1)*TH1x1**2*TH3x2*TH3x4 - 6*complex(0,1)*lam3*TH3x1**2*TH3x2*TH3x4 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH4x1**2 - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH4x1**2 - 2*complex(0,1)*lam4*TH3x2*TH3x4*TH4x1**2 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH4x1*TH4x2 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH4x1*TH4x2 - 4*complex(0,1)*lam4*TH3x1*TH3x4*TH4x1*TH4x2 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH4x1*TH4x4 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH4x1*TH4x4 - 4*complex(0,1)*lam4*TH3x1*TH3x2*TH4x1*TH4x4 - 2*alp1*complex(0,1)*TH1x1**2*TH4x2*TH4x4 - 2*alp2*complex(0,1)*TH1x1**2*TH4x2*TH4x4 - 2*complex(0,1)*lam4*TH3x1**2*TH4x2*TH4x4 - 6*complex(0,1)*lam3*TH4x1**2*TH4x2*TH4x4',
                  order = {'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x4 - 4*complex(0,1)*lam2*TH1x1*TH1x4 - 6*complex(0,1)*lam1*TH1x1*TH1x2**2*TH1x4 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH3x1*TH3x2 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH3x1*TH3x2 - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH3x2**2 - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH3x2**2 - 2*alp1*complex(0,1)*TH3x1*TH3x4 - 2*alp3*complex(0,1)*TH3x1*TH3x4 - 2*alp1*complex(0,1)*TH1x2**2*TH3x1*TH3x4 - 2*alp2*complex(0,1)*TH1x2**2*TH3x1*TH3x4 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH3x2*TH3x4 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH3x2*TH3x4 - 6*complex(0,1)*lam3*TH3x1*TH3x2**2*TH3x4 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH4x1*TH4x2 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH4x1*TH4x2 - 4*complex(0,1)*lam4*TH3x2*TH3x4*TH4x1*TH4x2 - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH4x2**2 - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH4x2**2 - 2*complex(0,1)*lam4*TH3x1*TH3x4*TH4x2**2 - 2*alp1*complex(0,1)*TH4x1*TH4x4 - 2*alp3*complex(0,1)*TH4x1*TH4x4 - 2*alp1*complex(0,1)*TH1x2**2*TH4x1*TH4x4 - 2*alp2*complex(0,1)*TH1x2**2*TH4x1*TH4x4 - 2*complex(0,1)*lam4*TH3x2**2*TH4x1*TH4x4 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH4x2*TH4x4 - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH4x2*TH4x4 - 4*complex(0,1)*lam4*TH3x1*TH3x2*TH4x2*TH4x4 - 6*complex(0,1)*lam3*TH4x1*TH4x2**2*TH4x4',
                  order = {'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x4 - 4*complex(0,1)*lam2*TH1x2*TH1x4 - 6*complex(0,1)*lam1*TH1x2**3*TH1x4 - 6*alp1*complex(0,1)*TH1x2*TH1x4*TH3x2**2 - 6*alp2*complex(0,1)*TH1x2*TH1x4*TH3x2**2 - 2*alp1*complex(0,1)*TH3x2*TH3x4 - 2*alp3*complex(0,1)*TH3x2*TH3x4 - 6*alp1*complex(0,1)*TH1x2**2*TH3x2*TH3x4 - 6*alp2*complex(0,1)*TH1x2**2*TH3x2*TH3x4 - 6*complex(0,1)*lam3*TH3x2**3*TH3x4 - 6*alp1*complex(0,1)*TH1x2*TH1x4*TH4x2**2 - 6*alp2*complex(0,1)*TH1x2*TH1x4*TH4x2**2 - 6*complex(0,1)*lam4*TH3x2*TH3x4*TH4x2**2 - 2*alp1*complex(0,1)*TH4x2*TH4x4 - 2*alp3*complex(0,1)*TH4x2*TH4x4 - 6*alp1*complex(0,1)*TH1x2**2*TH4x2*TH4x4 - 6*alp2*complex(0,1)*TH1x2**2*TH4x2*TH4x4 - 6*complex(0,1)*lam4*TH3x2**2*TH4x2*TH4x4 - 6*complex(0,1)*lam3*TH4x2**3*TH4x4',
                  order = {'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '-2*complex(0,1)*lam1*TH1x3*TH1x4 - 4*complex(0,1)*lam2*TH1x3*TH1x4 - 2*alp1*complex(0,1)*TH3x3*TH3x4 - 2*alp3*complex(0,1)*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH4x3*TH4x4 - 2*alp3*complex(0,1)*TH4x3*TH4x4',
                  order = {'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(complex(0,1)*gR**2*TH1x3*TH1x4)/2. + (complex(0,1)*gR**2*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x3*TH1x4)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x3*TH1x4 + (complex(0,1)*gL**2*sw**2*TH1x3*TH1x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x3*TH3x4)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x3*TH3x4 + (complex(0,1)*gL**2*sw**2*TH3x3*TH3x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x3*TH4x4)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x3*TH4x4 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x3*TH1x4)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x3*TH1x4)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x3*TH1x4)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x3*TH1x4)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x3*TH1x4)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x3*TH1x4)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x3*TH3x4)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x3*TH3x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x3*TH3x4)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x3*TH3x4)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x3*TH3x4)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x3*TH3x4)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x3*TH4x4)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x3*TH4x4)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x3*TH4x4)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x3*TH4x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x3*TH4x4)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x3*TH4x4 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x3*TH1x4)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x3*TH1x4)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x3*TH1x4)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x3*TH1x4)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x3*TH1x4)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x3*TH1x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x3*TH3x4)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x3*TH3x4)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x3*TH3x4)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x3*TH3x4)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x3*TH3x4)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x3*TH3x4)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x3*TH4x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x3*TH4x4)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x3*TH4x4)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x3*TH4x4)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x3*TH4x4)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x3*TH4x4 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x3*TH1x4)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x3*TH1x4 + (cph**2*complex(0,1)*gR**2*st**2*TH1x3*TH1x4)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x3*TH1x4 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x3*TH1x4 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x3*TH1x4)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x3*TH3x4)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x3*TH3x4 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x3*TH3x4)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x3*TH3x4 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x3*TH3x4 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x3*TH3x4)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x3*TH4x4)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x3*TH4x4 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x3*TH4x4)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x3*TH4x4 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x3*TH4x4 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x3*TH4x4 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x3*TH4x4 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x3*TH4x4)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x3*TH4x4 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x3*TH1x4)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x3*TH1x4)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x3*TH1x4)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x3*TH1x4)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x3*TH1x4)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x3*TH1x4 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x3*TH1x4)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x3*TH1x4)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x3*TH3x4)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x3*TH3x4)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x3*TH3x4)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x3*TH3x4)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x3*TH3x4)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x3*TH3x4 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x3*TH3x4)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x3*TH3x4)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x3*TH4x4)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x3*TH4x4 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x3*TH4x4)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x3*TH4x4)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x3*TH4x4)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x3*TH4x4)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x3*TH4x4)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x3*TH4x4)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x3*TH4x4)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x3*TH4x4)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x3*TH4x4)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x3*TH4x4)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x3*TH4x4 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x3*TH1x4)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x3*TH1x4 + (cw**2*complex(0,1)*gL**2*st**2*TH1x3*TH1x4)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x3*TH1x4 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x3*TH1x4 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x3*TH1x4)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x3*TH3x4)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x3*TH3x4 + (cw**2*complex(0,1)*gL**2*st**2*TH3x3*TH3x4)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x3*TH3x4 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x3*TH3x4 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x3*TH3x4)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x3*TH4x4)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x3*TH4x4 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x3*TH4x4)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x3*TH4x4 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x3*TH4x4 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x3*TH4x4 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x3*TH4x4 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x3*TH4x4)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x3*TH4x4 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x3*TH4x4)/2.',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '-6*complex(0,1)*lam1*TH1x1**2*TH1x3*TH1x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH3x1**2 - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH3x1**2 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH3x1*TH3x3 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH3x1*TH3x3 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH3x1*TH3x4 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH3x1*TH3x4 - 2*alp1*complex(0,1)*TH1x1**2*TH3x3*TH3x4 - 2*alp2*complex(0,1)*TH1x1**2*TH3x3*TH3x4 - 6*complex(0,1)*lam3*TH3x1**2*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH4x1**2 - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH4x1**2 - 2*complex(0,1)*lam4*TH3x3*TH3x4*TH4x1**2 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH4x1*TH4x3 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH4x1*TH4x3 - 4*complex(0,1)*lam4*TH3x1*TH3x4*TH4x1*TH4x3 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH4x1*TH4x4 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH4x1*TH4x4 - 4*complex(0,1)*lam4*TH3x1*TH3x3*TH4x1*TH4x4 - 2*alp1*complex(0,1)*TH1x1**2*TH4x3*TH4x4 - 2*alp2*complex(0,1)*TH1x1**2*TH4x3*TH4x4 - 2*complex(0,1)*lam4*TH3x1**2*TH4x3*TH4x4 - 6*complex(0,1)*lam3*TH4x1**2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x2*TH1x3*TH1x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH3x1*TH3x2 - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH3x1*TH3x2 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH3x1*TH3x3 - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH3x1*TH3x3 - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH3x2*TH3x3 - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH3x2*TH3x3 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH3x1*TH3x4 - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH3x1*TH3x4 - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH3x2*TH3x4 - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH3x2*TH3x4 - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH3x3*TH3x4 - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH3x3*TH3x4 - 6*complex(0,1)*lam3*TH3x1*TH3x2*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH4x1*TH4x2 - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH4x1*TH4x2 - 2*complex(0,1)*lam4*TH3x3*TH3x4*TH4x1*TH4x2 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH4x1*TH4x3 - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH4x1*TH4x3 - 2*complex(0,1)*lam4*TH3x2*TH3x4*TH4x1*TH4x3 - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH4x2*TH4x3 - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH4x2*TH4x3 - 2*complex(0,1)*lam4*TH3x1*TH3x4*TH4x2*TH4x3 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH4x1*TH4x4 - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH4x1*TH4x4 - 2*complex(0,1)*lam4*TH3x2*TH3x3*TH4x1*TH4x4 - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH4x2*TH4x4 - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH4x2*TH4x4 - 2*complex(0,1)*lam4*TH3x1*TH3x3*TH4x2*TH4x4 - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH4x3*TH4x4 - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH4x3*TH4x4 - 2*complex(0,1)*lam4*TH3x1*TH3x2*TH4x3*TH4x4 - 6*complex(0,1)*lam3*TH4x1*TH4x2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '-2*complex(0,1)*lam1*TH1x3*TH1x4 - 4*complex(0,1)*lam2*TH1x3*TH1x4 - 6*complex(0,1)*lam1*TH1x2**2*TH1x3*TH1x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH3x2**2 - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH3x2**2 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH3x2*TH3x3 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH3x2*TH3x3 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH3x2*TH3x4 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH3x2*TH3x4 - 2*alp1*complex(0,1)*TH3x3*TH3x4 - 2*alp3*complex(0,1)*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x2**2*TH3x3*TH3x4 - 2*alp2*complex(0,1)*TH1x2**2*TH3x3*TH3x4 - 6*complex(0,1)*lam3*TH3x2**2*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH4x2**2 - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH4x2**2 - 2*complex(0,1)*lam4*TH3x3*TH3x4*TH4x2**2 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH4x2*TH4x3 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH4x2*TH4x3 - 4*complex(0,1)*lam4*TH3x2*TH3x4*TH4x2*TH4x3 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH4x2*TH4x4 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH4x2*TH4x4 - 4*complex(0,1)*lam4*TH3x2*TH3x3*TH4x2*TH4x4 - 2*alp1*complex(0,1)*TH4x3*TH4x4 - 2*alp3*complex(0,1)*TH4x3*TH4x4 - 2*alp1*complex(0,1)*TH1x2**2*TH4x3*TH4x4 - 2*alp2*complex(0,1)*TH1x2**2*TH4x3*TH4x4 - 2*complex(0,1)*lam4*TH3x2**2*TH4x3*TH4x4 - 6*complex(0,1)*lam3*TH4x2**2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_310 = Coupling(name = 'GC_310',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x3**2*TH1x4 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH3x1*TH3x3 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH3x1*TH3x3 - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH3x3**2 - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH3x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x1*TH3x4 - 2*alp2*complex(0,1)*TH1x3**2*TH3x1*TH3x4 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH3x3*TH3x4 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH3x3*TH3x4 - 6*complex(0,1)*lam3*TH3x1*TH3x3**2*TH3x4 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH4x1*TH4x3 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH4x1*TH4x3 - 4*complex(0,1)*lam4*TH3x3*TH3x4*TH4x1*TH4x3 - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH4x3**2 - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH4x3**2 - 2*complex(0,1)*lam4*TH3x1*TH3x4*TH4x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH4x1*TH4x4 - 2*alp2*complex(0,1)*TH1x3**2*TH4x1*TH4x4 - 2*complex(0,1)*lam4*TH3x3**2*TH4x1*TH4x4 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH4x3*TH4x4 - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH4x3*TH4x4 - 4*complex(0,1)*lam4*TH3x1*TH3x3*TH4x3*TH4x4 - 6*complex(0,1)*lam3*TH4x1*TH4x3**2*TH4x4',
                  order = {'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '-6*complex(0,1)*lam1*TH1x2*TH1x3**2*TH1x4 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH3x2*TH3x3 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH3x2*TH3x3 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH3x3**2 - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH3x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x2*TH3x4 - 2*alp2*complex(0,1)*TH1x3**2*TH3x2*TH3x4 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH3x3*TH3x4 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH3x3*TH3x4 - 6*complex(0,1)*lam3*TH3x2*TH3x3**2*TH3x4 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH4x2*TH4x3 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH4x2*TH4x3 - 4*complex(0,1)*lam4*TH3x3*TH3x4*TH4x2*TH4x3 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH4x3**2 - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH4x3**2 - 2*complex(0,1)*lam4*TH3x2*TH3x4*TH4x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH4x2*TH4x4 - 2*alp2*complex(0,1)*TH1x3**2*TH4x2*TH4x4 - 2*complex(0,1)*lam4*TH3x3**2*TH4x2*TH4x4 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH4x3*TH4x4 - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH4x3*TH4x4 - 4*complex(0,1)*lam4*TH3x2*TH3x3*TH4x3*TH4x4 - 6*complex(0,1)*lam3*TH4x2*TH4x3**2*TH4x4',
                  order = {'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '-6*complex(0,1)*lam1*TH1x3**3*TH1x4 - 6*alp1*complex(0,1)*TH1x3*TH1x4*TH3x3**2 - 6*alp2*complex(0,1)*TH1x3*TH1x4*TH3x3**2 - 6*alp1*complex(0,1)*TH1x3**2*TH3x3*TH3x4 - 6*alp2*complex(0,1)*TH1x3**2*TH3x3*TH3x4 - 6*complex(0,1)*lam3*TH3x3**3*TH3x4 - 6*alp1*complex(0,1)*TH1x3*TH1x4*TH4x3**2 - 6*alp2*complex(0,1)*TH1x3*TH1x4*TH4x3**2 - 6*complex(0,1)*lam4*TH3x3*TH3x4*TH4x3**2 - 6*alp1*complex(0,1)*TH1x3**2*TH4x3*TH4x4 - 6*alp2*complex(0,1)*TH1x3**2*TH4x3*TH4x4 - 6*complex(0,1)*lam4*TH3x3**2*TH4x3*TH4x4 - 6*complex(0,1)*lam3*TH4x3**3*TH4x4',
                  order = {'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '-2*complex(0,1)*lam1*TH1x4**2 - 4*complex(0,1)*lam2*TH1x4**2 - 2*alp1*complex(0,1)*TH3x4**2 - 2*alp3*complex(0,1)*TH3x4**2 - 2*alp1*complex(0,1)*TH4x4**2 - 2*alp3*complex(0,1)*TH4x4**2',
                  order = {'QED':2})

GC_314 = Coupling(name = 'GC_314',
                  value = '(complex(0,1)*gR**2*TH1x4**2)/2. + (complex(0,1)*gR**2*TH4x4**2)/2.',
                  order = {'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*TH1x4**2)/2. - cw*complex(0,1)*gL*gR*sph*sw*TH1x4**2 + (complex(0,1)*gL**2*sw**2*TH1x4**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x4**2)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x4**2 + (complex(0,1)*gL**2*sw**2*TH3x4**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x4**2)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x4**2 + (cw**2*complex(0,1)*gR**2*sph**2*TH4x4**2)/2.',
                  order = {'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph*TH1x4**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH1x4**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH1x4**2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH1x4**2)/2. - (cph*complex(0,1)*gL*gR*st*sw*TH1x4**2)/2. + (ct*complex(0,1)*gL*gR*sph*sw**2*TH1x4**2)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x4**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x4**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x4**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x4**2)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x4**2)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x4**2)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x4**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x4**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x4**2)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x4**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x4**2)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x4**2 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x4**2)/2.',
                  order = {'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*TH1x4**2)/2. + (cw**2*complex(0,1)*gL*gR*sph*st*TH1x4**2)/2. - (cph*ct*complex(0,1)*gL*gR*sw*TH1x4**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH1x4**2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH1x4**2)/2. - (complex(0,1)*gL*gR*sph*st*sw**2*TH1x4**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x4**2)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x4**2)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x4**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x4**2)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x4**2)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x4**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x4**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x4**2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x4**2)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x4**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x4**2)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x4**2 + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x4**2)/2.',
                  order = {'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*TH1x4**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*TH1x4**2 + (cph**2*complex(0,1)*gR**2*st**2*TH1x4**2)/2. + ct**2*cw*complex(0,1)*gL*gR*sph*sw*TH1x4**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x4**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH1x4**2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x4**2)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x4**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH3x4**2)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x4**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x4**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x4**2)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x4**2)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x4**2 + (complex(0,1)*gBL**2*sph**2*st**2*TH4x4**2)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x4**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x4**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x4**2 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x4**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x4**2)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x4**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x4**2)/2.',
                  order = {'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*TH1x4**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH1x4**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH1x4**2)/2. + (cph*cw*complex(0,1)*gL*gR*st**2*TH1x4**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH1x4**2)/2. - ct*cw*complex(0,1)*gL*gR*sph*st*sw*TH1x4**2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH1x4**2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH1x4**2)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x4**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x4**2)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x4**2)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x4**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x4**2)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x4**2 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x4**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x4**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x4**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x4**2 + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x4**2)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x4**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x4**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x4**2)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x4**2)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x4**2)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x4**2)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x4**2)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x4**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x4**2)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x4**2 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x4**2)/2.',
                  order = {'QED':2})

GC_320 = Coupling(name = 'GC_320',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*TH1x4**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*TH1x4**2 + (cw**2*complex(0,1)*gL**2*st**2*TH1x4**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH1x4**2 + cw*complex(0,1)*gL*gR*sph*st**2*sw*TH1x4**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH1x4**2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x4**2)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x4**2 + (cw**2*complex(0,1)*gL**2*st**2*TH3x4**2)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x4**2 + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x4**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x4**2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x4**2)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x4**2 + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x4**2)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x4**2 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x4**2 + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x4**2 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x4**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x4**2)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x4**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x4**2)/2.',
                  order = {'QED':2})

GC_321 = Coupling(name = 'GC_321',
                  value = '-6*complex(0,1)*lam1*TH1x1**2*TH1x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x1**2 - 2*alp2*complex(0,1)*TH1x4**2*TH3x1**2 - 8*alp1*complex(0,1)*TH1x1*TH1x4*TH3x1*TH3x4 - 8*alp2*complex(0,1)*TH1x1*TH1x4*TH3x1*TH3x4 - 2*alp1*complex(0,1)*TH1x1**2*TH3x4**2 - 2*alp2*complex(0,1)*TH1x1**2*TH3x4**2 - 6*complex(0,1)*lam3*TH3x1**2*TH3x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH4x1**2 - 2*alp2*complex(0,1)*TH1x4**2*TH4x1**2 - 2*complex(0,1)*lam4*TH3x4**2*TH4x1**2 - 8*alp1*complex(0,1)*TH1x1*TH1x4*TH4x1*TH4x4 - 8*alp2*complex(0,1)*TH1x1*TH1x4*TH4x1*TH4x4 - 8*complex(0,1)*lam4*TH3x1*TH3x4*TH4x1*TH4x4 - 2*alp1*complex(0,1)*TH1x1**2*TH4x4**2 - 2*alp2*complex(0,1)*TH1x1**2*TH4x4**2 - 2*complex(0,1)*lam4*TH3x1**2*TH4x4**2 - 6*complex(0,1)*lam3*TH4x1**2*TH4x4**2',
                  order = {'QED':2})

GC_322 = Coupling(name = 'GC_322',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x2*TH1x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x1*TH3x2 - 2*alp2*complex(0,1)*TH1x4**2*TH3x1*TH3x2 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH3x1*TH3x4 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH3x1*TH3x4 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH3x2*TH3x4 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH3x2*TH3x4 - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH3x4**2 - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH3x4**2 - 6*complex(0,1)*lam3*TH3x1*TH3x2*TH3x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH4x1*TH4x2 - 2*alp2*complex(0,1)*TH1x4**2*TH4x1*TH4x2 - 2*complex(0,1)*lam4*TH3x4**2*TH4x1*TH4x2 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH4x1*TH4x4 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH4x1*TH4x4 - 4*complex(0,1)*lam4*TH3x2*TH3x4*TH4x1*TH4x4 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH4x2*TH4x4 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH4x2*TH4x4 - 4*complex(0,1)*lam4*TH3x1*TH3x4*TH4x2*TH4x4 - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH4x4**2 - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH4x4**2 - 2*complex(0,1)*lam4*TH3x1*TH3x2*TH4x4**2 - 6*complex(0,1)*lam3*TH4x1*TH4x2*TH4x4**2',
                  order = {'QED':2})

GC_323 = Coupling(name = 'GC_323',
                  value = '-2*complex(0,1)*lam1*TH1x4**2 - 4*complex(0,1)*lam2*TH1x4**2 - 6*complex(0,1)*lam1*TH1x2**2*TH1x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x2**2 - 2*alp2*complex(0,1)*TH1x4**2*TH3x2**2 - 8*alp1*complex(0,1)*TH1x2*TH1x4*TH3x2*TH3x4 - 8*alp2*complex(0,1)*TH1x2*TH1x4*TH3x2*TH3x4 - 2*alp1*complex(0,1)*TH3x4**2 - 2*alp3*complex(0,1)*TH3x4**2 - 2*alp1*complex(0,1)*TH1x2**2*TH3x4**2 - 2*alp2*complex(0,1)*TH1x2**2*TH3x4**2 - 6*complex(0,1)*lam3*TH3x2**2*TH3x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH4x2**2 - 2*alp2*complex(0,1)*TH1x4**2*TH4x2**2 - 2*complex(0,1)*lam4*TH3x4**2*TH4x2**2 - 8*alp1*complex(0,1)*TH1x2*TH1x4*TH4x2*TH4x4 - 8*alp2*complex(0,1)*TH1x2*TH1x4*TH4x2*TH4x4 - 8*complex(0,1)*lam4*TH3x2*TH3x4*TH4x2*TH4x4 - 2*alp1*complex(0,1)*TH4x4**2 - 2*alp3*complex(0,1)*TH4x4**2 - 2*alp1*complex(0,1)*TH1x2**2*TH4x4**2 - 2*alp2*complex(0,1)*TH1x2**2*TH4x4**2 - 2*complex(0,1)*lam4*TH3x2**2*TH4x4**2 - 6*complex(0,1)*lam3*TH4x2**2*TH4x4**2',
                  order = {'QED':2})

GC_324 = Coupling(name = 'GC_324',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x3*TH1x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x1*TH3x3 - 2*alp2*complex(0,1)*TH1x4**2*TH3x1*TH3x3 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH3x1*TH3x4 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH3x1*TH3x4 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH3x3*TH3x4 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH3x4**2 - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH3x4**2 - 6*complex(0,1)*lam3*TH3x1*TH3x3*TH3x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH4x1*TH4x3 - 2*alp2*complex(0,1)*TH1x4**2*TH4x1*TH4x3 - 2*complex(0,1)*lam4*TH3x4**2*TH4x1*TH4x3 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH4x1*TH4x4 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH4x1*TH4x4 - 4*complex(0,1)*lam4*TH3x3*TH3x4*TH4x1*TH4x4 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH4x3*TH4x4 - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH4x3*TH4x4 - 4*complex(0,1)*lam4*TH3x1*TH3x4*TH4x3*TH4x4 - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH4x4**2 - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH4x4**2 - 2*complex(0,1)*lam4*TH3x1*TH3x3*TH4x4**2 - 6*complex(0,1)*lam3*TH4x1*TH4x3*TH4x4**2',
                  order = {'QED':2})

GC_325 = Coupling(name = 'GC_325',
                  value = '-6*complex(0,1)*lam1*TH1x2*TH1x3*TH1x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x2*TH3x3 - 2*alp2*complex(0,1)*TH1x4**2*TH3x2*TH3x3 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH3x2*TH3x4 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH3x2*TH3x4 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH3x3*TH3x4 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH3x4**2 - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH3x4**2 - 6*complex(0,1)*lam3*TH3x2*TH3x3*TH3x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH4x2*TH4x3 - 2*alp2*complex(0,1)*TH1x4**2*TH4x2*TH4x3 - 2*complex(0,1)*lam4*TH3x4**2*TH4x2*TH4x3 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH4x2*TH4x4 - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH4x2*TH4x4 - 4*complex(0,1)*lam4*TH3x3*TH3x4*TH4x2*TH4x4 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH4x3*TH4x4 - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH4x3*TH4x4 - 4*complex(0,1)*lam4*TH3x2*TH3x4*TH4x3*TH4x4 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH4x4**2 - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH4x4**2 - 2*complex(0,1)*lam4*TH3x2*TH3x3*TH4x4**2 - 6*complex(0,1)*lam3*TH4x2*TH4x3*TH4x4**2',
                  order = {'QED':2})

GC_326 = Coupling(name = 'GC_326',
                  value = '-6*complex(0,1)*lam1*TH1x3**2*TH1x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x3**2 - 2*alp2*complex(0,1)*TH1x4**2*TH3x3**2 - 8*alp1*complex(0,1)*TH1x3*TH1x4*TH3x3*TH3x4 - 8*alp2*complex(0,1)*TH1x3*TH1x4*TH3x3*TH3x4 - 2*alp1*complex(0,1)*TH1x3**2*TH3x4**2 - 2*alp2*complex(0,1)*TH1x3**2*TH3x4**2 - 6*complex(0,1)*lam3*TH3x3**2*TH3x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH4x3**2 - 2*alp2*complex(0,1)*TH1x4**2*TH4x3**2 - 2*complex(0,1)*lam4*TH3x4**2*TH4x3**2 - 8*alp1*complex(0,1)*TH1x3*TH1x4*TH4x3*TH4x4 - 8*alp2*complex(0,1)*TH1x3*TH1x4*TH4x3*TH4x4 - 8*complex(0,1)*lam4*TH3x3*TH3x4*TH4x3*TH4x4 - 2*alp1*complex(0,1)*TH1x3**2*TH4x4**2 - 2*alp2*complex(0,1)*TH1x3**2*TH4x4**2 - 2*complex(0,1)*lam4*TH3x3**2*TH4x4**2 - 6*complex(0,1)*lam3*TH4x3**2*TH4x4**2',
                  order = {'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '-6*complex(0,1)*lam1*TH1x1*TH1x4**3 - 6*alp1*complex(0,1)*TH1x4**2*TH3x1*TH3x4 - 6*alp2*complex(0,1)*TH1x4**2*TH3x1*TH3x4 - 6*alp1*complex(0,1)*TH1x1*TH1x4*TH3x4**2 - 6*alp2*complex(0,1)*TH1x1*TH1x4*TH3x4**2 - 6*complex(0,1)*lam3*TH3x1*TH3x4**3 - 6*alp1*complex(0,1)*TH1x4**2*TH4x1*TH4x4 - 6*alp2*complex(0,1)*TH1x4**2*TH4x1*TH4x4 - 6*complex(0,1)*lam4*TH3x4**2*TH4x1*TH4x4 - 6*alp1*complex(0,1)*TH1x1*TH1x4*TH4x4**2 - 6*alp2*complex(0,1)*TH1x1*TH1x4*TH4x4**2 - 6*complex(0,1)*lam4*TH3x1*TH3x4*TH4x4**2 - 6*complex(0,1)*lam3*TH4x1*TH4x4**3',
                  order = {'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '-6*complex(0,1)*lam1*TH1x2*TH1x4**3 - 6*alp1*complex(0,1)*TH1x4**2*TH3x2*TH3x4 - 6*alp2*complex(0,1)*TH1x4**2*TH3x2*TH3x4 - 6*alp1*complex(0,1)*TH1x2*TH1x4*TH3x4**2 - 6*alp2*complex(0,1)*TH1x2*TH1x4*TH3x4**2 - 6*complex(0,1)*lam3*TH3x2*TH3x4**3 - 6*alp1*complex(0,1)*TH1x4**2*TH4x2*TH4x4 - 6*alp2*complex(0,1)*TH1x4**2*TH4x2*TH4x4 - 6*complex(0,1)*lam4*TH3x4**2*TH4x2*TH4x4 - 6*alp1*complex(0,1)*TH1x2*TH1x4*TH4x4**2 - 6*alp2*complex(0,1)*TH1x2*TH1x4*TH4x4**2 - 6*complex(0,1)*lam4*TH3x2*TH3x4*TH4x4**2 - 6*complex(0,1)*lam3*TH4x2*TH4x4**3',
                  order = {'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '-6*complex(0,1)*lam1*TH1x3*TH1x4**3 - 6*alp1*complex(0,1)*TH1x4**2*TH3x3*TH3x4 - 6*alp2*complex(0,1)*TH1x4**2*TH3x3*TH3x4 - 6*alp1*complex(0,1)*TH1x3*TH1x4*TH3x4**2 - 6*alp2*complex(0,1)*TH1x3*TH1x4*TH3x4**2 - 6*complex(0,1)*lam3*TH3x3*TH3x4**3 - 6*alp1*complex(0,1)*TH1x4**2*TH4x3*TH4x4 - 6*alp2*complex(0,1)*TH1x4**2*TH4x3*TH4x4 - 6*complex(0,1)*lam4*TH3x4**2*TH4x3*TH4x4 - 6*alp1*complex(0,1)*TH1x3*TH1x4*TH4x4**2 - 6*alp2*complex(0,1)*TH1x3*TH1x4*TH4x4**2 - 6*complex(0,1)*lam4*TH3x3*TH3x4*TH4x4**2 - 6*complex(0,1)*lam3*TH4x3*TH4x4**3',
                  order = {'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '-6*complex(0,1)*lam1*TH1x4**4 - 12*alp1*complex(0,1)*TH1x4**2*TH3x4**2 - 12*alp2*complex(0,1)*TH1x4**2*TH3x4**2 - 6*complex(0,1)*lam3*TH3x4**4 - 12*alp1*complex(0,1)*TH1x4**2*TH4x4**2 - 12*alp2*complex(0,1)*TH1x4**2*TH4x4**2 - 12*complex(0,1)*lam4*TH3x4**2*TH4x4**2 - 6*complex(0,1)*lam3*TH4x4**4',
                  order = {'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '-(gL*gR)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '-(complex(0,1)*gL*gR)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '(gL*gR)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '(-6*complex(0,1)*lam1)/(1 + tb**2 + tz**2)**2 - (12*alp1*complex(0,1)*tb**2)/(1 + tb**2 + tz**2)**2 - (12*alp2*complex(0,1)*tb**2)/(1 + tb**2 + tz**2)**2 - (6*complex(0,1)*lam3*tb**4)/(1 + tb**2 + tz**2)**2 - (12*alp1*complex(0,1)*tz**2)/(1 + tb**2 + tz**2)**2 - (12*alp2*complex(0,1)*tz**2)/(1 + tb**2 + tz**2)**2 - (12*complex(0,1)*lam4*tb**2*tz**2)/(1 + tb**2 + tz**2)**2 - (6*complex(0,1)*lam3*tz**4)/(1 + tb**2 + tz**2)**2',
                  order = {'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(complex(0,1)*gL**2)/(2.*(1 + tb**2 + tz**2)) + (complex(0,1)*gL**2*tb**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(-2*complex(0,1)*lam1)/(1 + tb**2 + tz**2) - (4*complex(0,1)*lam2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*tb**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tz**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(complex(0,1)*gR**2)/(2.*(1 + tb**2 + tz**2)) + (complex(0,1)*gR**2*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2)/(2.*(1 + tb**2 + tz**2)) - (cw*complex(0,1)*gL*gR*sph*sw)/(1 + tb**2 + tz**2) + (complex(0,1)*gL**2*sw**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*cw**2*complex(0,1)*gBL**2*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph*cw*complex(0,1)*gBL*gL*sw*tb**2)/(1 + tb**2 + tz**2) + (complex(0,1)*gL**2*sw**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*cw**2*complex(0,1)*gBL**2*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*cw**2*complex(0,1)*gBL*gR*sph*tz**2)/(1 + tb**2 + tz**2) + (cw**2*complex(0,1)*gR**2*sph**2*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*sph)/(2.*(1 + tb**2 + tz**2)) + (cph*cw*complex(0,1)*gR**2*sph*st)/(2.*(1 + tb**2 + tz**2)) + (ct*cw*complex(0,1)*gL**2*sw)/(2.*(1 + tb**2 + tz**2)) - (ct*cw*complex(0,1)*gR**2*sph**2*sw)/(2.*(1 + tb**2 + tz**2)) - (cph*complex(0,1)*gL*gR*st*sw)/(2.*(1 + tb**2 + tz**2)) + (ct*complex(0,1)*gL*gR*sph*sw**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*cw**2*complex(0,1)*gBL*gL*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph*cw*complex(0,1)*gBL**2*sph*st*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) + (ct*cw*complex(0,1)*gL**2*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) + (complex(0,1)*gBL*gL*sph*st*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*complex(0,1)*gBL*gL*sw**2*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*cw*complex(0,1)*gBL*gR*st*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*cw*complex(0,1)*gBL**2*sph*st*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*cw*complex(0,1)*gR**2*sph*st*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cw*complex(0,1)*gBL*gR*sph**2*st*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*tz**2)/(1 + tb**2 + tz**2) - (ct*cw*complex(0,1)*gR**2*sph**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph)/(2.*(1 + tb**2 + tz**2)) + (cw**2*complex(0,1)*gL*gR*sph*st)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*complex(0,1)*gL*gR*sw)/(2.*(1 + tb**2 + tz**2)) - (cw*complex(0,1)*gL**2*st*sw)/(2.*(1 + tb**2 + tz**2)) + (cw*complex(0,1)*gR**2*sph**2*st*sw)/(2.*(1 + tb**2 + tz**2)) - (complex(0,1)*gL*gR*sph*st*sw**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*cw*complex(0,1)*gBL**2*sph*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph*cw**2*complex(0,1)*gBL*gL*st*tb**2)/(2.*(1 + tb**2 + tz**2)) + (ct*complex(0,1)*gBL*gL*sph*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*cw*complex(0,1)*gBL**2*st*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cw*complex(0,1)*gL**2*st*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph*complex(0,1)*gBL*gL*st*sw**2*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*ct*cw*complex(0,1)*gBL*gR*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*cw*complex(0,1)*gBL**2*sph*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*cw*complex(0,1)*gR**2*sph*tz**2)/(2.*(1 + tb**2 + tz**2)) + (ct*cw*complex(0,1)*gBL*gR*sph**2*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*cw*complex(0,1)*gBL**2*st*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*cw*complex(0,1)*gBL*gR*sph*st*sw*tz**2)/(1 + tb**2 + tz**2) + (cw*complex(0,1)*gR**2*sph**2*st*sw*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*cw*complex(0,1)*gL*gR*st)/(1 + tb**2 + tz**2) + (cph**2*complex(0,1)*gR**2*st**2)/(2.*(1 + tb**2 + tz**2)) + (ct**2*cw*complex(0,1)*gL*gR*sph*sw)/(1 + tb**2 + tz**2) - (cph*ct*complex(0,1)*gR**2*sph*st*sw)/(1 + tb**2 + tz**2) + (ct**2*complex(0,1)*gR**2*sph**2*sw**2)/(2.*(1 + tb**2 + tz**2)) + (ct**2*cw**2*complex(0,1)*gL**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (ct*cw*complex(0,1)*gBL*gL*sph*st*tb**2)/(1 + tb**2 + tz**2) + (complex(0,1)*gBL**2*sph**2*st**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct**2*cw*complex(0,1)*gBL*gL*sw*tb**2)/(1 + tb**2 + tz**2) + (cph*ct*complex(0,1)*gBL**2*sph*st*sw*tb**2)/(1 + tb**2 + tz**2) + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*complex(0,1)*gR**2*st**2*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*complex(0,1)*gBL*gR*sph*st**2*tz**2)/(1 + tb**2 + tz**2) + (complex(0,1)*gBL**2*sph**2*st**2*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*ct*complex(0,1)*gBL*gR*st*sw*tz**2)/(1 + tb**2 + tz**2) + (cph*ct*complex(0,1)*gBL**2*sph*st*sw*tz**2)/(1 + tb**2 + tz**2) - (cph*ct*complex(0,1)*gR**2*sph*st*sw*tz**2)/(1 + tb**2 + tz**2) - (ct*complex(0,1)*gBL*gR*sph**2*st*sw*tz**2)/(1 + tb**2 + tz**2) + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*tz**2)/(1 + tb**2 + tz**2) + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR)/(2.*(1 + tb**2 + tz**2)) - (ct*cw**2*complex(0,1)*gL**2*st)/(2.*(1 + tb**2 + tz**2)) + (cph**2*ct*complex(0,1)*gR**2*st)/(2.*(1 + tb**2 + tz**2)) + (cph*cw*complex(0,1)*gL*gR*st**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct**2*complex(0,1)*gR**2*sph*sw)/(2.*(1 + tb**2 + tz**2)) - (ct*cw*complex(0,1)*gL*gR*sph*st*sw)/(1 + tb**2 + tz**2) + (cph*complex(0,1)*gR**2*sph*st**2*sw)/(2.*(1 + tb**2 + tz**2)) - (ct*complex(0,1)*gR**2*sph**2*st*sw**2)/(2.*(1 + tb**2 + tz**2)) + (ct**2*cw*complex(0,1)*gBL*gL*sph*tb**2)/(2.*(1 + tb**2 + tz**2)) - (ct*cw**2*complex(0,1)*gL**2*st*tb**2)/(2.*(1 + tb**2 + tz**2)) + (ct*complex(0,1)*gBL**2*sph**2*st*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cw*complex(0,1)*gBL*gL*sph*st**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*cw*complex(0,1)*gBL*gL*st*sw*tb**2)/(1 + tb**2 + tz**2) - (cph*complex(0,1)*gBL**2*sph*st**2*sw*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*ct*complex(0,1)*gR**2*st*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*complex(0,1)*gBL*gR*sph*st*tz**2)/(1 + tb**2 + tz**2) + (ct*complex(0,1)*gBL**2*sph**2*st*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct**2*complex(0,1)*gR**2*sph*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*complex(0,1)*gBL*gR*st**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*complex(0,1)*gBL**2*sph*st**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*complex(0,1)*gR**2*sph*st**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) + (complex(0,1)*gBL*gR*sph**2*st**2*sw*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*tz**2)/(1 + tb**2 + tz**2) - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*cw*complex(0,1)*gL*gR*st)/(1 + tb**2 + tz**2) + (cw**2*complex(0,1)*gL**2*st**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct*complex(0,1)*gR**2*sph*st*sw)/(1 + tb**2 + tz**2) + (cw*complex(0,1)*gL*gR*sph*st**2*sw)/(1 + tb**2 + tz**2) + (complex(0,1)*gR**2*sph**2*st**2*sw**2)/(2.*(1 + tb**2 + tz**2)) + (ct**2*complex(0,1)*gBL**2*sph**2*tb**2)/(2.*(1 + tb**2 + tz**2)) - (ct*cw*complex(0,1)*gBL*gL*sph*st*tb**2)/(1 + tb**2 + tz**2) + (cw**2*complex(0,1)*gL**2*st**2*tb**2)/(2.*(1 + tb**2 + tz**2)) - (cph*ct*complex(0,1)*gBL**2*sph*st*sw*tb**2)/(1 + tb**2 + tz**2) + (cph*cw*complex(0,1)*gBL*gL*st**2*sw*tb**2)/(1 + tb**2 + tz**2) + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*tb**2)/(2.*(1 + tb**2 + tz**2)) + (cph**2*ct**2*complex(0,1)*gR**2*tz**2)/(2.*(1 + tb**2 + tz**2)) + (cph*ct**2*complex(0,1)*gBL*gR*sph*tz**2)/(1 + tb**2 + tz**2) + (ct**2*complex(0,1)*gBL**2*sph**2*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph**2*ct*complex(0,1)*gBL*gR*st*sw*tz**2)/(1 + tb**2 + tz**2) - (cph*ct*complex(0,1)*gBL**2*sph*st*sw*tz**2)/(1 + tb**2 + tz**2) + (cph*ct*complex(0,1)*gR**2*sph*st*sw*tz**2)/(1 + tb**2 + tz**2) + (ct*complex(0,1)*gBL*gR*sph**2*st*sw*tz**2)/(1 + tb**2 + tz**2) + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*tz**2)/(2.*(1 + tb**2 + tz**2)) - (cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*tz**2)/(1 + tb**2 + tz**2) + (complex(0,1)*gR**2*sph**2*st**2*sw**2*tz**2)/(2.*(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '(-2*complex(0,1)*lam1*TH1x1**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x1**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x1**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x1**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x1**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x1**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x1**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x1**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x1**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x1**2*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x1**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x1**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x1**2*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '(-2*complex(0,1)*lam1*TH1x1*TH1x2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x1*TH1x2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x1*TH1x2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x1*TH3x2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x1*TH3x2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x1*TH3x2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x1*TH4x2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x1*TH4x2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x1*TH4x2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x1*TH1x2*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x1*TH1x2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x1*TH3x2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x1*TH4x2*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(-2*complex(0,1)*lam1)/(1 + tb**2 + tz**2) - (4*complex(0,1)*lam2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*tb**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam1*TH1x2**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x2**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x2**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x2**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x2**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x2**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x2**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x2**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x2**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tz**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*tz**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x2**2*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x2**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x2**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x2**2*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '(-2*complex(0,1)*lam1*TH1x1*TH1x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x1*TH1x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x1*TH1x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x1*TH3x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x1*TH3x3)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x1*TH3x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x1*TH4x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x1*TH4x3)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x1*TH4x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x1*TH1x3*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x1*TH1x3*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x1*TH3x3*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x1*TH4x3*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(-2*complex(0,1)*lam1*TH1x2*TH1x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x2*TH1x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x2*TH1x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x2*TH3x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x2*TH3x3)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x2*TH3x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x2*TH4x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x2*TH4x3)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x2*TH4x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x2*TH1x3*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x2*TH1x3*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x2*TH3x3*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x2*TH4x3*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '(-2*complex(0,1)*lam1*TH1x3**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x3**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x3**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x3**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x3**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x3**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x3**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x3**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x3**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x3**2*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x3**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x3**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x3**2*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '(-2*complex(0,1)*lam1*TH1x1*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x1*TH1x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x1*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x1*TH3x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x1*TH3x4)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x1*TH3x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x1*TH4x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x1*TH4x4)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x1*TH4x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x1*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x1*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x1*TH3x4*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x1*TH4x4*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_351 = Coupling(name = 'GC_351',
                  value = '(-2*complex(0,1)*lam1*TH1x2*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x2*TH1x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x2*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x2*TH3x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x2*TH3x4)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x2*TH3x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x2*TH4x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x2*TH4x4)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x2*TH4x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x2*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x2*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x2*TH3x4*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x2*TH4x4*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '(-2*complex(0,1)*lam1*TH1x3*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x3*TH1x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x3*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x3*TH3x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x3*TH3x4)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x3*TH3x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x3*TH4x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x3*TH4x4)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x3*TH4x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x3*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x3*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x3*TH3x4*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x3*TH4x4*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '(-2*complex(0,1)*lam1*TH1x4**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*TH1x4**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*TH1x4**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x4**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x4**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x4**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x4**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x4**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x4**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH1x4**2*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH1x4**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x4**2*tz**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x4**2*tz**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '(cw*gR*sph*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gL*sw*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*cw*gBL*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gL*sw*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*cw*gBL*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gR*sph*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '-(ct*cw*gL*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gR*st*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gR*sph*sw*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*cw*gL*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gBL*sph*st*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*ct*gBL*sw*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gR*st*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gBL*sph*st*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gBL*sw*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gR*sph*sw*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(cph*ct*gR*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cw*gL*st*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gR*sph*st*sw*TH1x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gBL*sph*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gL*st*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gBL*st*sw*tb*TH3x1)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gR*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gBL*sph*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gBL*st*sw*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gR*sph*st*sw*TH4x1*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(cw*gR*sph*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gL*sw*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*cw*gBL*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gL*sw*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*cw*gBL*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gR*sph*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '-(ct*cw*gL*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gR*st*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gR*sph*sw*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*cw*gL*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gBL*sph*st*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*ct*gBL*sw*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gR*st*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gBL*sph*st*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gBL*sw*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gR*sph*sw*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(cph*ct*gR*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cw*gL*st*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gR*sph*st*sw*TH1x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gBL*sph*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gL*st*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gBL*st*sw*tb*TH3x2)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gR*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gBL*sph*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gBL*st*sw*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gR*sph*st*sw*TH4x2*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(cw*gR*sph*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gL*sw*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*cw*gBL*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gL*sw*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*cw*gBL*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gR*sph*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-(ct*cw*gL*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gR*st*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gR*sph*sw*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*cw*gL*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gBL*sph*st*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*ct*gBL*sw*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gR*st*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gBL*sph*st*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gBL*sw*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gR*sph*sw*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cph*ct*gR*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cw*gL*st*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gR*sph*st*sw*TH1x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gBL*sph*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gL*st*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gBL*st*sw*tb*TH3x3)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gR*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gBL*sph*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gBL*st*sw*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gR*sph*st*sw*TH4x3*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(cw*gR*sph*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gL*sw*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*cw*gBL*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gL*sw*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*cw*gBL*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gR*sph*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '-(ct*cw*gL*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gR*st*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gR*sph*sw*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*cw*gL*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gBL*sph*st*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*ct*gBL*sw*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gR*st*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gBL*sph*st*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gBL*sw*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gR*sph*sw*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '(cph*ct*gR*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cw*gL*st*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gR*sph*st*sw*TH1x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gBL*sph*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cw*gL*st*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gBL*st*sw*tb*TH3x4)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gR*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gBL*sph*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gBL*st*sw*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gR*sph*st*sw*TH4x4*tz)/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(complex(0,1)*gL**2*kk*TH1x1)/2. + (complex(0,1)*gL**2*TH3x1*vL)/2.',
                  order = {'QED':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '(complex(0,1)*gL**2*kk*TH1x2)/2. + (complex(0,1)*gL**2*TH3x2*vL)/2.',
                  order = {'QED':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '(complex(0,1)*gL**2*kk*TH1x3)/2. + (complex(0,1)*gL**2*TH3x3*vL)/2.',
                  order = {'QED':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '(complex(0,1)*gL**2*kk*TH1x4)/2. + (complex(0,1)*gL**2*TH3x4*vL)/2.',
                  order = {'QED':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '-2*complex(0,1)*kk*lam1*TH1x1 - 4*complex(0,1)*kk*lam2*TH1x1 - 2*alp1*complex(0,1)*TH3x1*vL - 2*alp3*complex(0,1)*TH3x1*vL - 2*alp1*complex(0,1)*TH4x1*vR - 2*alp3*complex(0,1)*TH4x1*vR',
                  order = {'QED':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '(complex(0,1)*gR**2*kk*TH1x1)/2. + (complex(0,1)*gR**2*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '(cw**2*complex(0,1)*gR**2*kk*sph**2*TH1x1)/2. - cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x1 + (complex(0,1)*gL**2*kk*sw**2*TH1x1)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x1*vL)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x1*vL + (complex(0,1)*gL**2*sw**2*TH3x1*vL)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x1*vR)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x1*vR + (cw**2*complex(0,1)*gR**2*sph**2*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*kk*sph*TH1x1)/2. + (cph*cw*complex(0,1)*gR**2*kk*sph*st*TH1x1)/2. + (ct*cw*complex(0,1)*gL**2*kk*sw*TH1x1)/2. - (ct*cw*complex(0,1)*gR**2*kk*sph**2*sw*TH1x1)/2. - (cph*complex(0,1)*gL*gR*kk*st*sw*TH1x1)/2. + (ct*complex(0,1)*gL*gR*kk*sph*sw**2*TH1x1)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x1*vL)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x1*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x1*vL)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x1*vL)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x1*vL)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x1*vL)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x1*vR)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x1*vR)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x1*vR)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x1*vR)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x1*vR)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x1*vR - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*kk*sph*TH1x1)/2. + (cw**2*complex(0,1)*gL*gR*kk*sph*st*TH1x1)/2. - (cph*ct*complex(0,1)*gL*gR*kk*sw*TH1x1)/2. - (cw*complex(0,1)*gL**2*kk*st*sw*TH1x1)/2. + (cw*complex(0,1)*gR**2*kk*sph**2*st*sw*TH1x1)/2. - (complex(0,1)*gL*gR*kk*sph*st*sw**2*TH1x1)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x1*vL)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x1*vL)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x1*vL)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x1*vL)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x1*vL)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x1*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x1*vR)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x1*vR)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x1*vR)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x1*vR)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x1*vR)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x1*vR + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*kk*TH1x1)/2. - cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x1 + (cph**2*complex(0,1)*gR**2*kk*st**2*TH1x1)/2. + ct**2*cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x1 - cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x1 + (ct**2*complex(0,1)*gR**2*kk*sph**2*sw**2*TH1x1)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x1*vL)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*vL + (complex(0,1)*gBL**2*sph**2*st**2*TH3x1*vL)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x1*vL + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*vL + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x1*vL)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x1*vR)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x1*vR + (complex(0,1)*gBL**2*sph**2*st**2*TH4x1*vR)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*vR + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*vR - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*vR - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*vR + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x1*vR)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x1*vR + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*kk*TH1x1)/2. - (ct*cw**2*complex(0,1)*gL**2*kk*st*TH1x1)/2. + (cph**2*ct*complex(0,1)*gR**2*kk*st*TH1x1)/2. + (cph*cw*complex(0,1)*gL*gR*kk*st**2*TH1x1)/2. - (cph*ct**2*complex(0,1)*gR**2*kk*sph*sw*TH1x1)/2. - ct*cw*complex(0,1)*gL*gR*kk*sph*st*sw*TH1x1 + (cph*complex(0,1)*gR**2*kk*sph*st**2*sw*TH1x1)/2. - (ct*complex(0,1)*gR**2*kk*sph**2*st*sw**2*TH1x1)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x1*vL)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x1*vL)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x1*vL)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x1*vL)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x1*vL)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x1*vL - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x1*vL)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x1*vL)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x1*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x1*vR + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x1*vR)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x1*vR)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x1*vR)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x1*vR)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x1*vR)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x1*vR)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x1*vR)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x1*vR)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x1*vR)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x1*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x1*vR - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*kk*TH1x1)/2. + cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x1 + (cw**2*complex(0,1)*gL**2*kk*st**2*TH1x1)/2. + cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x1 + cw*complex(0,1)*gL*gR*kk*sph*st**2*sw*TH1x1 + (complex(0,1)*gR**2*kk*sph**2*st**2*sw**2*TH1x1)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x1*vL)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x1*vL + (cw**2*complex(0,1)*gL**2*st**2*TH3x1*vL)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x1*vL + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x1*vL + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x1*vL)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x1*vR)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x1*vR + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x1*vR)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x1*vR - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x1*vR + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x1*vR + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x1*vR + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x1*vR)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x1*vR + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x1*vR)/2.',
                  order = {'QED':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1**3 - 6*alp1*complex(0,1)*kk*TH1x1*TH3x1**2 - 6*alp2*complex(0,1)*kk*TH1x1*TH3x1**2 - 6*alp1*complex(0,1)*kk*TH1x1*TH4x1**2 - 6*alp2*complex(0,1)*kk*TH1x1*TH4x1**2 - 6*alp1*complex(0,1)*TH1x1**2*TH3x1*vL - 6*alp2*complex(0,1)*TH1x1**2*TH3x1*vL - 6*complex(0,1)*lam3*TH3x1**3*vL - 6*complex(0,1)*lam4*TH3x1*TH4x1**2*vL - 6*alp1*complex(0,1)*TH1x1**2*TH4x1*vR - 6*alp2*complex(0,1)*TH1x1**2*TH4x1*vR - 6*complex(0,1)*lam4*TH3x1**2*TH4x1*vR - 6*complex(0,1)*lam3*TH4x1**3*vR - 3*complex(0,1)*kap*TH1x1*TH3x1*TH4x1*cmath.sqrt(2)',
                  order = {'QED':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '-2*complex(0,1)*kk*lam1*TH1x2 - 4*complex(0,1)*kk*lam2*TH1x2 - 2*alp1*complex(0,1)*TH3x2*vL - 2*alp3*complex(0,1)*TH3x2*vL - 2*alp1*complex(0,1)*TH4x2*vR - 2*alp3*complex(0,1)*TH4x2*vR',
                  order = {'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '(complex(0,1)*gR**2*kk*TH1x2)/2. + (complex(0,1)*gR**2*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '(cw**2*complex(0,1)*gR**2*kk*sph**2*TH1x2)/2. - cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x2 + (complex(0,1)*gL**2*kk*sw**2*TH1x2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x2*vL)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x2*vL + (complex(0,1)*gL**2*sw**2*TH3x2*vL)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x2*vR)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x2*vR + (cw**2*complex(0,1)*gR**2*sph**2*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*kk*sph*TH1x2)/2. + (cph*cw*complex(0,1)*gR**2*kk*sph*st*TH1x2)/2. + (ct*cw*complex(0,1)*gL**2*kk*sw*TH1x2)/2. - (ct*cw*complex(0,1)*gR**2*kk*sph**2*sw*TH1x2)/2. - (cph*complex(0,1)*gL*gR*kk*st*sw*TH1x2)/2. + (ct*complex(0,1)*gL*gR*kk*sph*sw**2*TH1x2)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x2*vL)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x2*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x2*vL)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x2*vL)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x2*vL)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x2*vL)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x2*vR)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x2*vR)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x2*vR)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x2*vR)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x2*vR)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x2*vR - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*kk*sph*TH1x2)/2. + (cw**2*complex(0,1)*gL*gR*kk*sph*st*TH1x2)/2. - (cph*ct*complex(0,1)*gL*gR*kk*sw*TH1x2)/2. - (cw*complex(0,1)*gL**2*kk*st*sw*TH1x2)/2. + (cw*complex(0,1)*gR**2*kk*sph**2*st*sw*TH1x2)/2. - (complex(0,1)*gL*gR*kk*sph*st*sw**2*TH1x2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x2*vL)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x2*vL)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x2*vL)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x2*vL)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x2*vL)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x2*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x2*vR)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x2*vR)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x2*vR)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x2*vR)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x2*vR)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x2*vR + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*kk*TH1x2)/2. - cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x2 + (cph**2*complex(0,1)*gR**2*kk*st**2*TH1x2)/2. + ct**2*cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x2 - cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x2 + (ct**2*complex(0,1)*gR**2*kk*sph**2*sw**2*TH1x2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x2*vL)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2*vL + (complex(0,1)*gBL**2*sph**2*st**2*TH3x2*vL)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x2*vL + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2*vL + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x2*vL)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x2*vR)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x2*vR + (complex(0,1)*gBL**2*sph**2*st**2*TH4x2*vR)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2*vR + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2*vR - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2*vR - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2*vR + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x2*vR)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x2*vR + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*kk*TH1x2)/2. - (ct*cw**2*complex(0,1)*gL**2*kk*st*TH1x2)/2. + (cph**2*ct*complex(0,1)*gR**2*kk*st*TH1x2)/2. + (cph*cw*complex(0,1)*gL*gR*kk*st**2*TH1x2)/2. - (cph*ct**2*complex(0,1)*gR**2*kk*sph*sw*TH1x2)/2. - ct*cw*complex(0,1)*gL*gR*kk*sph*st*sw*TH1x2 + (cph*complex(0,1)*gR**2*kk*sph*st**2*sw*TH1x2)/2. - (ct*complex(0,1)*gR**2*kk*sph**2*st*sw**2*TH1x2)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x2*vL)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x2*vL)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x2*vL)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x2*vL)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x2*vL)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x2*vL - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x2*vL)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x2*vL)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x2*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x2*vR + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x2*vR)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x2*vR)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x2*vR)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x2*vR)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x2*vR)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x2*vR)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x2*vR)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x2*vR)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x2*vR)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x2*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x2*vR - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*kk*TH1x2)/2. + cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x2 + (cw**2*complex(0,1)*gL**2*kk*st**2*TH1x2)/2. + cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x2 + cw*complex(0,1)*gL*gR*kk*sph*st**2*sw*TH1x2 + (complex(0,1)*gR**2*kk*sph**2*st**2*sw**2*TH1x2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x2*vL)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x2*vL + (cw**2*complex(0,1)*gL**2*st**2*TH3x2*vL)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x2*vL + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x2*vL + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x2*vL)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x2*vR)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x2*vR + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x2*vR)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x2*vR - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x2*vR + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x2*vR + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x2*vR + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x2*vR)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x2*vR + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x2*vR)/2.',
                  order = {'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1**2*TH1x2 - 2*alp1*complex(0,1)*kk*TH1x2*TH3x1**2 - 2*alp2*complex(0,1)*kk*TH1x2*TH3x1**2 - 4*alp1*complex(0,1)*kk*TH1x1*TH3x1*TH3x2 - 4*alp2*complex(0,1)*kk*TH1x1*TH3x1*TH3x2 - 2*alp1*complex(0,1)*kk*TH1x2*TH4x1**2 - 2*alp2*complex(0,1)*kk*TH1x2*TH4x1**2 - 4*alp1*complex(0,1)*kk*TH1x1*TH4x1*TH4x2 - 4*alp2*complex(0,1)*kk*TH1x1*TH4x1*TH4x2 - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH3x1*vL - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH3x1*vL - 2*alp1*complex(0,1)*TH1x1**2*TH3x2*vL - 2*alp2*complex(0,1)*TH1x1**2*TH3x2*vL - 6*complex(0,1)*lam3*TH3x1**2*TH3x2*vL - 2*complex(0,1)*lam4*TH3x2*TH4x1**2*vL - 4*complex(0,1)*lam4*TH3x1*TH4x1*TH4x2*vL - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH4x1*vR - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH4x1*vR - 4*complex(0,1)*lam4*TH3x1*TH3x2*TH4x1*vR - 2*alp1*complex(0,1)*TH1x1**2*TH4x2*vR - 2*alp2*complex(0,1)*TH1x1**2*TH4x2*vR - 2*complex(0,1)*lam4*TH3x1**2*TH4x2*vR - 6*complex(0,1)*lam3*TH4x1**2*TH4x2*vR - complex(0,1)*kap*TH1x2*TH3x1*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x2*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x1*TH4x2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '-2*complex(0,1)*kk*lam1*TH1x1 - 4*complex(0,1)*kk*lam2*TH1x1 - 6*complex(0,1)*kk*lam1*TH1x1*TH1x2**2 - 4*alp1*complex(0,1)*kk*TH1x2*TH3x1*TH3x2 - 4*alp2*complex(0,1)*kk*TH1x2*TH3x1*TH3x2 - 2*alp1*complex(0,1)*kk*TH1x1*TH3x2**2 - 2*alp2*complex(0,1)*kk*TH1x1*TH3x2**2 - 4*alp1*complex(0,1)*kk*TH1x2*TH4x1*TH4x2 - 4*alp2*complex(0,1)*kk*TH1x2*TH4x1*TH4x2 - 2*alp1*complex(0,1)*kk*TH1x1*TH4x2**2 - 2*alp2*complex(0,1)*kk*TH1x1*TH4x2**2 - 2*alp1*complex(0,1)*TH3x1*vL - 2*alp3*complex(0,1)*TH3x1*vL - 2*alp1*complex(0,1)*TH1x2**2*TH3x1*vL - 2*alp2*complex(0,1)*TH1x2**2*TH3x1*vL - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH3x2*vL - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH3x2*vL - 6*complex(0,1)*lam3*TH3x1*TH3x2**2*vL - 4*complex(0,1)*lam4*TH3x2*TH4x1*TH4x2*vL - 2*complex(0,1)*lam4*TH3x1*TH4x2**2*vL - 2*alp1*complex(0,1)*TH4x1*vR - 2*alp3*complex(0,1)*TH4x1*vR - 2*alp1*complex(0,1)*TH1x2**2*TH4x1*vR - 2*alp2*complex(0,1)*TH1x2**2*TH4x1*vR - 2*complex(0,1)*lam4*TH3x2**2*TH4x1*vR - 4*alp1*complex(0,1)*TH1x1*TH1x2*TH4x2*vR - 4*alp2*complex(0,1)*TH1x1*TH1x2*TH4x2*vR - 4*complex(0,1)*lam4*TH3x1*TH3x2*TH4x2*vR - 6*complex(0,1)*lam3*TH4x1*TH4x2**2*vR - complex(0,1)*kap*TH1x2*TH3x2*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x1*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x2*TH4x2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '-2*complex(0,1)*kk*lam1*TH1x2 - 4*complex(0,1)*kk*lam2*TH1x2 - 6*complex(0,1)*kk*lam1*TH1x2**3 - 6*alp1*complex(0,1)*kk*TH1x2*TH3x2**2 - 6*alp2*complex(0,1)*kk*TH1x2*TH3x2**2 - 6*alp1*complex(0,1)*kk*TH1x2*TH4x2**2 - 6*alp2*complex(0,1)*kk*TH1x2*TH4x2**2 - 2*alp1*complex(0,1)*TH3x2*vL - 2*alp3*complex(0,1)*TH3x2*vL - 6*alp1*complex(0,1)*TH1x2**2*TH3x2*vL - 6*alp2*complex(0,1)*TH1x2**2*TH3x2*vL - 6*complex(0,1)*lam3*TH3x2**3*vL - 6*complex(0,1)*lam4*TH3x2*TH4x2**2*vL - 2*alp1*complex(0,1)*TH4x2*vR - 2*alp3*complex(0,1)*TH4x2*vR - 6*alp1*complex(0,1)*TH1x2**2*TH4x2*vR - 6*alp2*complex(0,1)*TH1x2**2*TH4x2*vR - 6*complex(0,1)*lam4*TH3x2**2*TH4x2*vR - 6*complex(0,1)*lam3*TH4x2**3*vR - 3*complex(0,1)*kap*TH1x2*TH3x2*TH4x2*cmath.sqrt(2)',
                  order = {'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '-2*complex(0,1)*kk*lam1*TH1x3 - 4*complex(0,1)*kk*lam2*TH1x3 - 2*alp1*complex(0,1)*TH3x3*vL - 2*alp3*complex(0,1)*TH3x3*vL - 2*alp1*complex(0,1)*TH4x3*vR - 2*alp3*complex(0,1)*TH4x3*vR',
                  order = {'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '(complex(0,1)*gR**2*kk*TH1x3)/2. + (complex(0,1)*gR**2*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(cw**2*complex(0,1)*gR**2*kk*sph**2*TH1x3)/2. - cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x3 + (complex(0,1)*gL**2*kk*sw**2*TH1x3)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x3*vL)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x3*vL + (complex(0,1)*gL**2*sw**2*TH3x3*vL)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x3*vR)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x3*vR + (cw**2*complex(0,1)*gR**2*sph**2*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*kk*sph*TH1x3)/2. + (cph*cw*complex(0,1)*gR**2*kk*sph*st*TH1x3)/2. + (ct*cw*complex(0,1)*gL**2*kk*sw*TH1x3)/2. - (ct*cw*complex(0,1)*gR**2*kk*sph**2*sw*TH1x3)/2. - (cph*complex(0,1)*gL*gR*kk*st*sw*TH1x3)/2. + (ct*complex(0,1)*gL*gR*kk*sph*sw**2*TH1x3)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x3*vL)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x3*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x3*vL)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x3*vL)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x3*vL)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x3*vL)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x3*vR)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x3*vR)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x3*vR)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x3*vR)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x3*vR)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x3*vR - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*kk*sph*TH1x3)/2. + (cw**2*complex(0,1)*gL*gR*kk*sph*st*TH1x3)/2. - (cph*ct*complex(0,1)*gL*gR*kk*sw*TH1x3)/2. - (cw*complex(0,1)*gL**2*kk*st*sw*TH1x3)/2. + (cw*complex(0,1)*gR**2*kk*sph**2*st*sw*TH1x3)/2. - (complex(0,1)*gL*gR*kk*sph*st*sw**2*TH1x3)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x3*vL)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x3*vL)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x3*vL)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x3*vL)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x3*vL)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x3*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x3*vR)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x3*vR)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x3*vR)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x3*vR)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x3*vR)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x3*vR + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*kk*TH1x3)/2. - cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x3 + (cph**2*complex(0,1)*gR**2*kk*st**2*TH1x3)/2. + ct**2*cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x3 - cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x3 + (ct**2*complex(0,1)*gR**2*kk*sph**2*sw**2*TH1x3)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x3*vL)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x3*vL + (complex(0,1)*gBL**2*sph**2*st**2*TH3x3*vL)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x3*vL + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x3*vL + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x3*vL)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x3*vR)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x3*vR + (complex(0,1)*gBL**2*sph**2*st**2*TH4x3*vR)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x3*vR + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x3*vR - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x3*vR - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x3*vR + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x3*vR)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x3*vR + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*kk*TH1x3)/2. - (ct*cw**2*complex(0,1)*gL**2*kk*st*TH1x3)/2. + (cph**2*ct*complex(0,1)*gR**2*kk*st*TH1x3)/2. + (cph*cw*complex(0,1)*gL*gR*kk*st**2*TH1x3)/2. - (cph*ct**2*complex(0,1)*gR**2*kk*sph*sw*TH1x3)/2. - ct*cw*complex(0,1)*gL*gR*kk*sph*st*sw*TH1x3 + (cph*complex(0,1)*gR**2*kk*sph*st**2*sw*TH1x3)/2. - (ct*complex(0,1)*gR**2*kk*sph**2*st*sw**2*TH1x3)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x3*vL)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x3*vL)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x3*vL)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x3*vL)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x3*vL)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x3*vL - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x3*vL)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x3*vL)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x3*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x3*vR + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x3*vR)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x3*vR)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x3*vR)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x3*vR)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x3*vR)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x3*vR)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x3*vR)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x3*vR)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x3*vR)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x3*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x3*vR - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*kk*TH1x3)/2. + cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x3 + (cw**2*complex(0,1)*gL**2*kk*st**2*TH1x3)/2. + cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x3 + cw*complex(0,1)*gL*gR*kk*sph*st**2*sw*TH1x3 + (complex(0,1)*gR**2*kk*sph**2*st**2*sw**2*TH1x3)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x3*vL)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x3*vL + (cw**2*complex(0,1)*gL**2*st**2*TH3x3*vL)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x3*vL + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x3*vL + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x3*vL)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x3*vR)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x3*vR + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x3*vR)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x3*vR - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x3*vR + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x3*vR + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x3*vR + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x3*vR)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x3*vR + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x3*vR)/2.',
                  order = {'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1**2*TH1x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH3x1**2 - 2*alp2*complex(0,1)*kk*TH1x3*TH3x1**2 - 4*alp1*complex(0,1)*kk*TH1x1*TH3x1*TH3x3 - 4*alp2*complex(0,1)*kk*TH1x1*TH3x1*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH4x1**2 - 2*alp2*complex(0,1)*kk*TH1x3*TH4x1**2 - 4*alp1*complex(0,1)*kk*TH1x1*TH4x1*TH4x3 - 4*alp2*complex(0,1)*kk*TH1x1*TH4x1*TH4x3 - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH3x1*vL - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH3x1*vL - 2*alp1*complex(0,1)*TH1x1**2*TH3x3*vL - 2*alp2*complex(0,1)*TH1x1**2*TH3x3*vL - 6*complex(0,1)*lam3*TH3x1**2*TH3x3*vL - 2*complex(0,1)*lam4*TH3x3*TH4x1**2*vL - 4*complex(0,1)*lam4*TH3x1*TH4x1*TH4x3*vL - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH4x1*vR - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH4x1*vR - 4*complex(0,1)*lam4*TH3x1*TH3x3*TH4x1*vR - 2*alp1*complex(0,1)*TH1x1**2*TH4x3*vR - 2*alp2*complex(0,1)*TH1x1**2*TH4x3*vR - 2*complex(0,1)*lam4*TH3x1**2*TH4x3*vR - 6*complex(0,1)*lam3*TH4x1**2*TH4x3*vR - complex(0,1)*kap*TH1x3*TH3x1*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x3*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x1*TH4x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1*TH1x2*TH1x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH3x1*TH3x2 - 2*alp2*complex(0,1)*kk*TH1x3*TH3x1*TH3x2 - 2*alp1*complex(0,1)*kk*TH1x2*TH3x1*TH3x3 - 2*alp2*complex(0,1)*kk*TH1x2*TH3x1*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x1*TH3x2*TH3x3 - 2*alp2*complex(0,1)*kk*TH1x1*TH3x2*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH4x1*TH4x2 - 2*alp2*complex(0,1)*kk*TH1x3*TH4x1*TH4x2 - 2*alp1*complex(0,1)*kk*TH1x2*TH4x1*TH4x3 - 2*alp2*complex(0,1)*kk*TH1x2*TH4x1*TH4x3 - 2*alp1*complex(0,1)*kk*TH1x1*TH4x2*TH4x3 - 2*alp2*complex(0,1)*kk*TH1x1*TH4x2*TH4x3 - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH3x1*vL - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH3x1*vL - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH3x2*vL - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH3x2*vL - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH3x3*vL - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH3x3*vL - 6*complex(0,1)*lam3*TH3x1*TH3x2*TH3x3*vL - 2*complex(0,1)*lam4*TH3x3*TH4x1*TH4x2*vL - 2*complex(0,1)*lam4*TH3x2*TH4x1*TH4x3*vL - 2*complex(0,1)*lam4*TH3x1*TH4x2*TH4x3*vL - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH4x1*vR - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH4x1*vR - 2*complex(0,1)*lam4*TH3x2*TH3x3*TH4x1*vR - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH4x2*vR - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH4x2*vR - 2*complex(0,1)*lam4*TH3x1*TH3x3*TH4x2*vR - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH4x3*vR - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH4x3*vR - 2*complex(0,1)*lam4*TH3x1*TH3x2*TH4x3*vR - 6*complex(0,1)*lam3*TH4x1*TH4x2*TH4x3*vR - (complex(0,1)*kap*TH1x3*TH3x2*TH4x1)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x2*TH3x3*TH4x1)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x3*TH3x1*TH4x2)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x1*TH3x3*TH4x2)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x2*TH3x1*TH4x3)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x1*TH3x2*TH4x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '-2*complex(0,1)*kk*lam1*TH1x3 - 4*complex(0,1)*kk*lam2*TH1x3 - 6*complex(0,1)*kk*lam1*TH1x2**2*TH1x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH3x2**2 - 2*alp2*complex(0,1)*kk*TH1x3*TH3x2**2 - 4*alp1*complex(0,1)*kk*TH1x2*TH3x2*TH3x3 - 4*alp2*complex(0,1)*kk*TH1x2*TH3x2*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH4x2**2 - 2*alp2*complex(0,1)*kk*TH1x3*TH4x2**2 - 4*alp1*complex(0,1)*kk*TH1x2*TH4x2*TH4x3 - 4*alp2*complex(0,1)*kk*TH1x2*TH4x2*TH4x3 - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH3x2*vL - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH3x2*vL - 2*alp1*complex(0,1)*TH3x3*vL - 2*alp3*complex(0,1)*TH3x3*vL - 2*alp1*complex(0,1)*TH1x2**2*TH3x3*vL - 2*alp2*complex(0,1)*TH1x2**2*TH3x3*vL - 6*complex(0,1)*lam3*TH3x2**2*TH3x3*vL - 2*complex(0,1)*lam4*TH3x3*TH4x2**2*vL - 4*complex(0,1)*lam4*TH3x2*TH4x2*TH4x3*vL - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH4x2*vR - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH4x2*vR - 4*complex(0,1)*lam4*TH3x2*TH3x3*TH4x2*vR - 2*alp1*complex(0,1)*TH4x3*vR - 2*alp3*complex(0,1)*TH4x3*vR - 2*alp1*complex(0,1)*TH1x2**2*TH4x3*vR - 2*alp2*complex(0,1)*TH1x2**2*TH4x3*vR - 2*complex(0,1)*lam4*TH3x2**2*TH4x3*vR - 6*complex(0,1)*lam3*TH4x2**2*TH4x3*vR - complex(0,1)*kap*TH1x3*TH3x2*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x3*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x2*TH4x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1*TH1x3**2 - 4*alp1*complex(0,1)*kk*TH1x3*TH3x1*TH3x3 - 4*alp2*complex(0,1)*kk*TH1x3*TH3x1*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x1*TH3x3**2 - 2*alp2*complex(0,1)*kk*TH1x1*TH3x3**2 - 4*alp1*complex(0,1)*kk*TH1x3*TH4x1*TH4x3 - 4*alp2*complex(0,1)*kk*TH1x3*TH4x1*TH4x3 - 2*alp1*complex(0,1)*kk*TH1x1*TH4x3**2 - 2*alp2*complex(0,1)*kk*TH1x1*TH4x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x1*vL - 2*alp2*complex(0,1)*TH1x3**2*TH3x1*vL - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH3x3*vL - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH3x3*vL - 6*complex(0,1)*lam3*TH3x1*TH3x3**2*vL - 4*complex(0,1)*lam4*TH3x3*TH4x1*TH4x3*vL - 2*complex(0,1)*lam4*TH3x1*TH4x3**2*vL - 2*alp1*complex(0,1)*TH1x3**2*TH4x1*vR - 2*alp2*complex(0,1)*TH1x3**2*TH4x1*vR - 2*complex(0,1)*lam4*TH3x3**2*TH4x1*vR - 4*alp1*complex(0,1)*TH1x1*TH1x3*TH4x3*vR - 4*alp2*complex(0,1)*TH1x1*TH1x3*TH4x3*vR - 4*complex(0,1)*lam4*TH3x1*TH3x3*TH4x3*vR - 6*complex(0,1)*lam3*TH4x1*TH4x3**2*vR - complex(0,1)*kap*TH1x3*TH3x3*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x3*TH3x1*TH4x3*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x3*TH4x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '-6*complex(0,1)*kk*lam1*TH1x2*TH1x3**2 - 4*alp1*complex(0,1)*kk*TH1x3*TH3x2*TH3x3 - 4*alp2*complex(0,1)*kk*TH1x3*TH3x2*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x2*TH3x3**2 - 2*alp2*complex(0,1)*kk*TH1x2*TH3x3**2 - 4*alp1*complex(0,1)*kk*TH1x3*TH4x2*TH4x3 - 4*alp2*complex(0,1)*kk*TH1x3*TH4x2*TH4x3 - 2*alp1*complex(0,1)*kk*TH1x2*TH4x3**2 - 2*alp2*complex(0,1)*kk*TH1x2*TH4x3**2 - 2*alp1*complex(0,1)*TH1x3**2*TH3x2*vL - 2*alp2*complex(0,1)*TH1x3**2*TH3x2*vL - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH3x3*vL - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH3x3*vL - 6*complex(0,1)*lam3*TH3x2*TH3x3**2*vL - 4*complex(0,1)*lam4*TH3x3*TH4x2*TH4x3*vL - 2*complex(0,1)*lam4*TH3x2*TH4x3**2*vL - 2*alp1*complex(0,1)*TH1x3**2*TH4x2*vR - 2*alp2*complex(0,1)*TH1x3**2*TH4x2*vR - 2*complex(0,1)*lam4*TH3x3**2*TH4x2*vR - 4*alp1*complex(0,1)*TH1x2*TH1x3*TH4x3*vR - 4*alp2*complex(0,1)*TH1x2*TH1x3*TH4x3*vR - 4*complex(0,1)*lam4*TH3x2*TH3x3*TH4x3*vR - 6*complex(0,1)*lam3*TH4x2*TH4x3**2*vR - complex(0,1)*kap*TH1x3*TH3x3*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x3*TH3x2*TH4x3*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x3*TH4x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '-6*complex(0,1)*kk*lam1*TH1x3**3 - 6*alp1*complex(0,1)*kk*TH1x3*TH3x3**2 - 6*alp2*complex(0,1)*kk*TH1x3*TH3x3**2 - 6*alp1*complex(0,1)*kk*TH1x3*TH4x3**2 - 6*alp2*complex(0,1)*kk*TH1x3*TH4x3**2 - 6*alp1*complex(0,1)*TH1x3**2*TH3x3*vL - 6*alp2*complex(0,1)*TH1x3**2*TH3x3*vL - 6*complex(0,1)*lam3*TH3x3**3*vL - 6*complex(0,1)*lam4*TH3x3*TH4x3**2*vL - 6*alp1*complex(0,1)*TH1x3**2*TH4x3*vR - 6*alp2*complex(0,1)*TH1x3**2*TH4x3*vR - 6*complex(0,1)*lam4*TH3x3**2*TH4x3*vR - 6*complex(0,1)*lam3*TH4x3**3*vR - 3*complex(0,1)*kap*TH1x3*TH3x3*TH4x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '-2*complex(0,1)*kk*lam1*TH1x4 - 4*complex(0,1)*kk*lam2*TH1x4 - 2*alp1*complex(0,1)*TH3x4*vL - 2*alp3*complex(0,1)*TH3x4*vL - 2*alp1*complex(0,1)*TH4x4*vR - 2*alp3*complex(0,1)*TH4x4*vR',
                  order = {'QED':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '(complex(0,1)*gR**2*kk*TH1x4)/2. + (complex(0,1)*gR**2*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '(cw**2*complex(0,1)*gR**2*kk*sph**2*TH1x4)/2. - cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x4 + (complex(0,1)*gL**2*kk*sw**2*TH1x4)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH3x4*vL)/2. - cph*cw*complex(0,1)*gBL*gL*sw*TH3x4*vL + (complex(0,1)*gL**2*sw**2*TH3x4*vL)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*TH4x4*vR)/2. - cph*cw**2*complex(0,1)*gBL*gR*sph*TH4x4*vR + (cw**2*complex(0,1)*gR**2*sph**2*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '-(ct*cw**2*complex(0,1)*gL*gR*kk*sph*TH1x4)/2. + (cph*cw*complex(0,1)*gR**2*kk*sph*st*TH1x4)/2. + (ct*cw*complex(0,1)*gL**2*kk*sw*TH1x4)/2. - (ct*cw*complex(0,1)*gR**2*kk*sph**2*sw*TH1x4)/2. - (cph*complex(0,1)*gL*gR*kk*st*sw*TH1x4)/2. + (ct*complex(0,1)*gL*gR*kk*sph*sw**2*TH1x4)/2. - (cph*ct*cw**2*complex(0,1)*gBL*gL*TH3x4*vL)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH3x4*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH3x4*vL)/2. + (ct*cw*complex(0,1)*gL**2*sw*TH3x4*vL)/2. + (complex(0,1)*gBL*gL*sph*st*sw*TH3x4*vL)/2. + (cph*ct*complex(0,1)*gBL*gL*sw**2*TH3x4*vL)/2. - (cph**2*cw*complex(0,1)*gBL*gR*st*TH4x4*vR)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*TH4x4*vR)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*TH4x4*vR)/2. + (cw*complex(0,1)*gBL*gR*sph**2*st*TH4x4*vR)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*TH4x4*vR)/2. + cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*TH4x4*vR - (ct*cw*complex(0,1)*gR**2*sph**2*sw*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*kk*sph*TH1x4)/2. + (cw**2*complex(0,1)*gL*gR*kk*sph*st*TH1x4)/2. - (cph*ct*complex(0,1)*gL*gR*kk*sw*TH1x4)/2. - (cw*complex(0,1)*gL**2*kk*st*sw*TH1x4)/2. + (cw*complex(0,1)*gR**2*kk*sph**2*st*sw*TH1x4)/2. - (complex(0,1)*gL*gR*kk*sph*st*sw**2*TH1x4)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH3x4*vL)/2. + (cph*cw**2*complex(0,1)*gBL*gL*st*TH3x4*vL)/2. + (ct*complex(0,1)*gBL*gL*sph*sw*TH3x4*vL)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH3x4*vL)/2. - (cw*complex(0,1)*gL**2*st*sw*TH3x4*vL)/2. - (cph*complex(0,1)*gBL*gL*st*sw**2*TH3x4*vL)/2. - (cph**2*ct*cw*complex(0,1)*gBL*gR*TH4x4*vR)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*TH4x4*vR)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*TH4x4*vR)/2. + (ct*cw*complex(0,1)*gBL*gR*sph**2*TH4x4*vR)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*TH4x4*vR)/2. - cph*cw*complex(0,1)*gBL*gR*sph*st*sw*TH4x4*vR + (cw*complex(0,1)*gR**2*sph**2*st*sw*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*kk*TH1x4)/2. - cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x4 + (cph**2*complex(0,1)*gR**2*kk*st**2*TH1x4)/2. + ct**2*cw*complex(0,1)*gL*gR*kk*sph*sw*TH1x4 - cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x4 + (ct**2*complex(0,1)*gR**2*kk*sph**2*sw**2*TH1x4)/2. + (ct**2*cw**2*complex(0,1)*gL**2*TH3x4*vL)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x4*vL + (complex(0,1)*gBL**2*sph**2*st**2*TH3x4*vL)/2. + cph*ct**2*cw*complex(0,1)*gBL*gL*sw*TH3x4*vL + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x4*vL + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH3x4*vL)/2. + (cph**2*complex(0,1)*gR**2*st**2*TH4x4*vR)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*TH4x4*vR + (complex(0,1)*gBL**2*sph**2*st**2*TH4x4*vR)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x4*vR + cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x4*vR - cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x4*vR - ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x4*vR + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*TH4x4*vR)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*TH4x4*vR + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-(cph*ct**2*cw*complex(0,1)*gL*gR*kk*TH1x4)/2. - (ct*cw**2*complex(0,1)*gL**2*kk*st*TH1x4)/2. + (cph**2*ct*complex(0,1)*gR**2*kk*st*TH1x4)/2. + (cph*cw*complex(0,1)*gL*gR*kk*st**2*TH1x4)/2. - (cph*ct**2*complex(0,1)*gR**2*kk*sph*sw*TH1x4)/2. - ct*cw*complex(0,1)*gL*gR*kk*sph*st*sw*TH1x4 + (cph*complex(0,1)*gR**2*kk*sph*st**2*sw*TH1x4)/2. - (ct*complex(0,1)*gR**2*kk*sph**2*st*sw**2*TH1x4)/2. + (ct**2*cw*complex(0,1)*gBL*gL*sph*TH3x4*vL)/2. - (ct*cw**2*complex(0,1)*gL**2*st*TH3x4*vL)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*TH3x4*vL)/2. - (cw*complex(0,1)*gBL*gL*sph*st**2*TH3x4*vL)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH3x4*vL)/2. - cph*ct*cw*complex(0,1)*gBL*gL*st*sw*TH3x4*vL - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH3x4*vL)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH3x4*vL)/2. + (cph**2*ct*complex(0,1)*gR**2*st*TH4x4*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*TH4x4*vR + (ct*complex(0,1)*gBL**2*sph**2*st*TH4x4*vR)/2. + (cph**2*ct**2*complex(0,1)*gBL*gR*sw*TH4x4*vR)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*TH4x4*vR)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*TH4x4*vR)/2. - (ct**2*complex(0,1)*gBL*gR*sph**2*sw*TH4x4*vR)/2. - (cph**2*complex(0,1)*gBL*gR*st**2*sw*TH4x4*vR)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*TH4x4*vR)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*TH4x4*vR)/2. + (complex(0,1)*gBL*gR*sph**2*st**2*sw*TH4x4*vR)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*TH4x4*vR)/2. + cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*TH4x4*vR - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*kk*TH1x4)/2. + cph*ct*cw*complex(0,1)*gL*gR*kk*st*TH1x4 + (cw**2*complex(0,1)*gL**2*kk*st**2*TH1x4)/2. + cph*ct*complex(0,1)*gR**2*kk*sph*st*sw*TH1x4 + cw*complex(0,1)*gL*gR*kk*sph*st**2*sw*TH1x4 + (complex(0,1)*gR**2*kk*sph**2*st**2*sw**2*TH1x4)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*TH3x4*vL)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*TH3x4*vL + (cw**2*complex(0,1)*gL**2*st**2*TH3x4*vL)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH3x4*vL + cph*cw*complex(0,1)*gBL*gL*st**2*sw*TH3x4*vL + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH3x4*vL)/2. + (cph**2*ct**2*complex(0,1)*gR**2*TH4x4*vR)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*TH4x4*vR + (ct**2*complex(0,1)*gBL**2*sph**2*TH4x4*vR)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*TH4x4*vR - cph*ct*complex(0,1)*gBL**2*sph*st*sw*TH4x4*vR + cph*ct*complex(0,1)*gR**2*sph*st*sw*TH4x4*vR + ct*complex(0,1)*gBL*gR*sph**2*st*sw*TH4x4*vR + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*TH4x4*vR)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*TH4x4*vR + (complex(0,1)*gR**2*sph**2*st**2*sw**2*TH4x4*vR)/2.',
                  order = {'QED':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1**2*TH1x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH3x1**2 - 2*alp2*complex(0,1)*kk*TH1x4*TH3x1**2 - 4*alp1*complex(0,1)*kk*TH1x1*TH3x1*TH3x4 - 4*alp2*complex(0,1)*kk*TH1x1*TH3x1*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH4x1**2 - 2*alp2*complex(0,1)*kk*TH1x4*TH4x1**2 - 4*alp1*complex(0,1)*kk*TH1x1*TH4x1*TH4x4 - 4*alp2*complex(0,1)*kk*TH1x1*TH4x1*TH4x4 - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH3x1*vL - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH3x1*vL - 2*alp1*complex(0,1)*TH1x1**2*TH3x4*vL - 2*alp2*complex(0,1)*TH1x1**2*TH3x4*vL - 6*complex(0,1)*lam3*TH3x1**2*TH3x4*vL - 2*complex(0,1)*lam4*TH3x4*TH4x1**2*vL - 4*complex(0,1)*lam4*TH3x1*TH4x1*TH4x4*vL - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH4x1*vR - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH4x1*vR - 4*complex(0,1)*lam4*TH3x1*TH3x4*TH4x1*vR - 2*alp1*complex(0,1)*TH1x1**2*TH4x4*vR - 2*alp2*complex(0,1)*TH1x1**2*TH4x4*vR - 2*complex(0,1)*lam4*TH3x1**2*TH4x4*vR - 6*complex(0,1)*lam3*TH4x1**2*TH4x4*vR - complex(0,1)*kap*TH1x4*TH3x1*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x4*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x1*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1*TH1x2*TH1x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH3x1*TH3x2 - 2*alp2*complex(0,1)*kk*TH1x4*TH3x1*TH3x2 - 2*alp1*complex(0,1)*kk*TH1x2*TH3x1*TH3x4 - 2*alp2*complex(0,1)*kk*TH1x2*TH3x1*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x1*TH3x2*TH3x4 - 2*alp2*complex(0,1)*kk*TH1x1*TH3x2*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH4x1*TH4x2 - 2*alp2*complex(0,1)*kk*TH1x4*TH4x1*TH4x2 - 2*alp1*complex(0,1)*kk*TH1x2*TH4x1*TH4x4 - 2*alp2*complex(0,1)*kk*TH1x2*TH4x1*TH4x4 - 2*alp1*complex(0,1)*kk*TH1x1*TH4x2*TH4x4 - 2*alp2*complex(0,1)*kk*TH1x1*TH4x2*TH4x4 - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH3x1*vL - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH3x1*vL - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH3x2*vL - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH3x2*vL - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH3x4*vL - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH3x4*vL - 6*complex(0,1)*lam3*TH3x1*TH3x2*TH3x4*vL - 2*complex(0,1)*lam4*TH3x4*TH4x1*TH4x2*vL - 2*complex(0,1)*lam4*TH3x2*TH4x1*TH4x4*vL - 2*complex(0,1)*lam4*TH3x1*TH4x2*TH4x4*vL - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH4x1*vR - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH4x1*vR - 2*complex(0,1)*lam4*TH3x2*TH3x4*TH4x1*vR - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH4x2*vR - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH4x2*vR - 2*complex(0,1)*lam4*TH3x1*TH3x4*TH4x2*vR - 2*alp1*complex(0,1)*TH1x1*TH1x2*TH4x4*vR - 2*alp2*complex(0,1)*TH1x1*TH1x2*TH4x4*vR - 2*complex(0,1)*lam4*TH3x1*TH3x2*TH4x4*vR - 6*complex(0,1)*lam3*TH4x1*TH4x2*TH4x4*vR - (complex(0,1)*kap*TH1x4*TH3x2*TH4x1)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x2*TH3x4*TH4x1)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x4*TH3x1*TH4x2)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x1*TH3x4*TH4x2)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x2*TH3x1*TH4x4)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x1*TH3x2*TH4x4)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '-2*complex(0,1)*kk*lam1*TH1x4 - 4*complex(0,1)*kk*lam2*TH1x4 - 6*complex(0,1)*kk*lam1*TH1x2**2*TH1x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH3x2**2 - 2*alp2*complex(0,1)*kk*TH1x4*TH3x2**2 - 4*alp1*complex(0,1)*kk*TH1x2*TH3x2*TH3x4 - 4*alp2*complex(0,1)*kk*TH1x2*TH3x2*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH4x2**2 - 2*alp2*complex(0,1)*kk*TH1x4*TH4x2**2 - 4*alp1*complex(0,1)*kk*TH1x2*TH4x2*TH4x4 - 4*alp2*complex(0,1)*kk*TH1x2*TH4x2*TH4x4 - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH3x2*vL - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH3x2*vL - 2*alp1*complex(0,1)*TH3x4*vL - 2*alp3*complex(0,1)*TH3x4*vL - 2*alp1*complex(0,1)*TH1x2**2*TH3x4*vL - 2*alp2*complex(0,1)*TH1x2**2*TH3x4*vL - 6*complex(0,1)*lam3*TH3x2**2*TH3x4*vL - 2*complex(0,1)*lam4*TH3x4*TH4x2**2*vL - 4*complex(0,1)*lam4*TH3x2*TH4x2*TH4x4*vL - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH4x2*vR - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH4x2*vR - 4*complex(0,1)*lam4*TH3x2*TH3x4*TH4x2*vR - 2*alp1*complex(0,1)*TH4x4*vR - 2*alp3*complex(0,1)*TH4x4*vR - 2*alp1*complex(0,1)*TH1x2**2*TH4x4*vR - 2*alp2*complex(0,1)*TH1x2**2*TH4x4*vR - 2*complex(0,1)*lam4*TH3x2**2*TH4x4*vR - 6*complex(0,1)*lam3*TH4x2**2*TH4x4*vR - complex(0,1)*kap*TH1x4*TH3x2*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x4*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x2*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_415 = Coupling(name = 'GC_415',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1*TH1x3*TH1x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH3x1*TH3x3 - 2*alp2*complex(0,1)*kk*TH1x4*TH3x1*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH3x1*TH3x4 - 2*alp2*complex(0,1)*kk*TH1x3*TH3x1*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x1*TH3x3*TH3x4 - 2*alp2*complex(0,1)*kk*TH1x1*TH3x3*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH4x1*TH4x3 - 2*alp2*complex(0,1)*kk*TH1x4*TH4x1*TH4x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH4x1*TH4x4 - 2*alp2*complex(0,1)*kk*TH1x3*TH4x1*TH4x4 - 2*alp1*complex(0,1)*kk*TH1x1*TH4x3*TH4x4 - 2*alp2*complex(0,1)*kk*TH1x1*TH4x3*TH4x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH3x1*vL - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH3x1*vL - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH3x3*vL - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH3x3*vL - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH3x4*vL - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH3x4*vL - 6*complex(0,1)*lam3*TH3x1*TH3x3*TH3x4*vL - 2*complex(0,1)*lam4*TH3x4*TH4x1*TH4x3*vL - 2*complex(0,1)*lam4*TH3x3*TH4x1*TH4x4*vL - 2*complex(0,1)*lam4*TH3x1*TH4x3*TH4x4*vL - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH4x1*vR - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH4x1*vR - 2*complex(0,1)*lam4*TH3x3*TH3x4*TH4x1*vR - 2*alp1*complex(0,1)*TH1x1*TH1x4*TH4x3*vR - 2*alp2*complex(0,1)*TH1x1*TH1x4*TH4x3*vR - 2*complex(0,1)*lam4*TH3x1*TH3x4*TH4x3*vR - 2*alp1*complex(0,1)*TH1x1*TH1x3*TH4x4*vR - 2*alp2*complex(0,1)*TH1x1*TH1x3*TH4x4*vR - 2*complex(0,1)*lam4*TH3x1*TH3x3*TH4x4*vR - 6*complex(0,1)*lam3*TH4x1*TH4x3*TH4x4*vR - (complex(0,1)*kap*TH1x4*TH3x3*TH4x1)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x3*TH3x4*TH4x1)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x4*TH3x1*TH4x3)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x1*TH3x4*TH4x3)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x3*TH3x1*TH4x4)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x1*TH3x3*TH4x4)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '-6*complex(0,1)*kk*lam1*TH1x2*TH1x3*TH1x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH3x2*TH3x3 - 2*alp2*complex(0,1)*kk*TH1x4*TH3x2*TH3x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH3x2*TH3x4 - 2*alp2*complex(0,1)*kk*TH1x3*TH3x2*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x2*TH3x3*TH3x4 - 2*alp2*complex(0,1)*kk*TH1x2*TH3x3*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH4x2*TH4x3 - 2*alp2*complex(0,1)*kk*TH1x4*TH4x2*TH4x3 - 2*alp1*complex(0,1)*kk*TH1x3*TH4x2*TH4x4 - 2*alp2*complex(0,1)*kk*TH1x3*TH4x2*TH4x4 - 2*alp1*complex(0,1)*kk*TH1x2*TH4x3*TH4x4 - 2*alp2*complex(0,1)*kk*TH1x2*TH4x3*TH4x4 - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH3x2*vL - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH3x2*vL - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH3x3*vL - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH3x3*vL - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH3x4*vL - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH3x4*vL - 6*complex(0,1)*lam3*TH3x2*TH3x3*TH3x4*vL - 2*complex(0,1)*lam4*TH3x4*TH4x2*TH4x3*vL - 2*complex(0,1)*lam4*TH3x3*TH4x2*TH4x4*vL - 2*complex(0,1)*lam4*TH3x2*TH4x3*TH4x4*vL - 2*alp1*complex(0,1)*TH1x3*TH1x4*TH4x2*vR - 2*alp2*complex(0,1)*TH1x3*TH1x4*TH4x2*vR - 2*complex(0,1)*lam4*TH3x3*TH3x4*TH4x2*vR - 2*alp1*complex(0,1)*TH1x2*TH1x4*TH4x3*vR - 2*alp2*complex(0,1)*TH1x2*TH1x4*TH4x3*vR - 2*complex(0,1)*lam4*TH3x2*TH3x4*TH4x3*vR - 2*alp1*complex(0,1)*TH1x2*TH1x3*TH4x4*vR - 2*alp2*complex(0,1)*TH1x2*TH1x3*TH4x4*vR - 2*complex(0,1)*lam4*TH3x2*TH3x3*TH4x4*vR - 6*complex(0,1)*lam3*TH4x2*TH4x3*TH4x4*vR - (complex(0,1)*kap*TH1x4*TH3x3*TH4x2)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x3*TH3x4*TH4x2)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x4*TH3x2*TH4x3)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x2*TH3x4*TH4x3)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x3*TH3x2*TH4x4)/cmath.sqrt(2) - (complex(0,1)*kap*TH1x2*TH3x3*TH4x4)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '-6*complex(0,1)*kk*lam1*TH1x3**2*TH1x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH3x3**2 - 2*alp2*complex(0,1)*kk*TH1x4*TH3x3**2 - 4*alp1*complex(0,1)*kk*TH1x3*TH3x3*TH3x4 - 4*alp2*complex(0,1)*kk*TH1x3*TH3x3*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x4*TH4x3**2 - 2*alp2*complex(0,1)*kk*TH1x4*TH4x3**2 - 4*alp1*complex(0,1)*kk*TH1x3*TH4x3*TH4x4 - 4*alp2*complex(0,1)*kk*TH1x3*TH4x3*TH4x4 - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH3x3*vL - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH3x3*vL - 2*alp1*complex(0,1)*TH1x3**2*TH3x4*vL - 2*alp2*complex(0,1)*TH1x3**2*TH3x4*vL - 6*complex(0,1)*lam3*TH3x3**2*TH3x4*vL - 2*complex(0,1)*lam4*TH3x4*TH4x3**2*vL - 4*complex(0,1)*lam4*TH3x3*TH4x3*TH4x4*vL - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH4x3*vR - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH4x3*vR - 4*complex(0,1)*lam4*TH3x3*TH3x4*TH4x3*vR - 2*alp1*complex(0,1)*TH1x3**2*TH4x4*vR - 2*alp2*complex(0,1)*TH1x3**2*TH4x4*vR - 2*complex(0,1)*lam4*TH3x3**2*TH4x4*vR - 6*complex(0,1)*lam3*TH4x3**2*TH4x4*vR - complex(0,1)*kap*TH1x4*TH3x3*TH4x3*cmath.sqrt(2) - complex(0,1)*kap*TH1x3*TH3x4*TH4x3*cmath.sqrt(2) - complex(0,1)*kap*TH1x3*TH3x3*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '-6*complex(0,1)*kk*lam1*TH1x1*TH1x4**2 - 4*alp1*complex(0,1)*kk*TH1x4*TH3x1*TH3x4 - 4*alp2*complex(0,1)*kk*TH1x4*TH3x1*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x1*TH3x4**2 - 2*alp2*complex(0,1)*kk*TH1x1*TH3x4**2 - 4*alp1*complex(0,1)*kk*TH1x4*TH4x1*TH4x4 - 4*alp2*complex(0,1)*kk*TH1x4*TH4x1*TH4x4 - 2*alp1*complex(0,1)*kk*TH1x1*TH4x4**2 - 2*alp2*complex(0,1)*kk*TH1x1*TH4x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x1*vL - 2*alp2*complex(0,1)*TH1x4**2*TH3x1*vL - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH3x4*vL - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH3x4*vL - 6*complex(0,1)*lam3*TH3x1*TH3x4**2*vL - 4*complex(0,1)*lam4*TH3x4*TH4x1*TH4x4*vL - 2*complex(0,1)*lam4*TH3x1*TH4x4**2*vL - 2*alp1*complex(0,1)*TH1x4**2*TH4x1*vR - 2*alp2*complex(0,1)*TH1x4**2*TH4x1*vR - 2*complex(0,1)*lam4*TH3x4**2*TH4x1*vR - 4*alp1*complex(0,1)*TH1x1*TH1x4*TH4x4*vR - 4*alp2*complex(0,1)*TH1x1*TH1x4*TH4x4*vR - 4*complex(0,1)*lam4*TH3x1*TH3x4*TH4x4*vR - 6*complex(0,1)*lam3*TH4x1*TH4x4**2*vR - complex(0,1)*kap*TH1x4*TH3x4*TH4x1*cmath.sqrt(2) - complex(0,1)*kap*TH1x4*TH3x1*TH4x4*cmath.sqrt(2) - complex(0,1)*kap*TH1x1*TH3x4*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '-6*complex(0,1)*kk*lam1*TH1x2*TH1x4**2 - 4*alp1*complex(0,1)*kk*TH1x4*TH3x2*TH3x4 - 4*alp2*complex(0,1)*kk*TH1x4*TH3x2*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x2*TH3x4**2 - 2*alp2*complex(0,1)*kk*TH1x2*TH3x4**2 - 4*alp1*complex(0,1)*kk*TH1x4*TH4x2*TH4x4 - 4*alp2*complex(0,1)*kk*TH1x4*TH4x2*TH4x4 - 2*alp1*complex(0,1)*kk*TH1x2*TH4x4**2 - 2*alp2*complex(0,1)*kk*TH1x2*TH4x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x2*vL - 2*alp2*complex(0,1)*TH1x4**2*TH3x2*vL - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH3x4*vL - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH3x4*vL - 6*complex(0,1)*lam3*TH3x2*TH3x4**2*vL - 4*complex(0,1)*lam4*TH3x4*TH4x2*TH4x4*vL - 2*complex(0,1)*lam4*TH3x2*TH4x4**2*vL - 2*alp1*complex(0,1)*TH1x4**2*TH4x2*vR - 2*alp2*complex(0,1)*TH1x4**2*TH4x2*vR - 2*complex(0,1)*lam4*TH3x4**2*TH4x2*vR - 4*alp1*complex(0,1)*TH1x2*TH1x4*TH4x4*vR - 4*alp2*complex(0,1)*TH1x2*TH1x4*TH4x4*vR - 4*complex(0,1)*lam4*TH3x2*TH3x4*TH4x4*vR - 6*complex(0,1)*lam3*TH4x2*TH4x4**2*vR - complex(0,1)*kap*TH1x4*TH3x4*TH4x2*cmath.sqrt(2) - complex(0,1)*kap*TH1x4*TH3x2*TH4x4*cmath.sqrt(2) - complex(0,1)*kap*TH1x2*TH3x4*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '-6*complex(0,1)*kk*lam1*TH1x3*TH1x4**2 - 4*alp1*complex(0,1)*kk*TH1x4*TH3x3*TH3x4 - 4*alp2*complex(0,1)*kk*TH1x4*TH3x3*TH3x4 - 2*alp1*complex(0,1)*kk*TH1x3*TH3x4**2 - 2*alp2*complex(0,1)*kk*TH1x3*TH3x4**2 - 4*alp1*complex(0,1)*kk*TH1x4*TH4x3*TH4x4 - 4*alp2*complex(0,1)*kk*TH1x4*TH4x3*TH4x4 - 2*alp1*complex(0,1)*kk*TH1x3*TH4x4**2 - 2*alp2*complex(0,1)*kk*TH1x3*TH4x4**2 - 2*alp1*complex(0,1)*TH1x4**2*TH3x3*vL - 2*alp2*complex(0,1)*TH1x4**2*TH3x3*vL - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH3x4*vL - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH3x4*vL - 6*complex(0,1)*lam3*TH3x3*TH3x4**2*vL - 4*complex(0,1)*lam4*TH3x4*TH4x3*TH4x4*vL - 2*complex(0,1)*lam4*TH3x3*TH4x4**2*vL - 2*alp1*complex(0,1)*TH1x4**2*TH4x3*vR - 2*alp2*complex(0,1)*TH1x4**2*TH4x3*vR - 2*complex(0,1)*lam4*TH3x4**2*TH4x3*vR - 4*alp1*complex(0,1)*TH1x3*TH1x4*TH4x4*vR - 4*alp2*complex(0,1)*TH1x3*TH1x4*TH4x4*vR - 4*complex(0,1)*lam4*TH3x3*TH3x4*TH4x4*vR - 6*complex(0,1)*lam3*TH4x3*TH4x4**2*vR - complex(0,1)*kap*TH1x4*TH3x4*TH4x3*cmath.sqrt(2) - complex(0,1)*kap*TH1x4*TH3x3*TH4x4*cmath.sqrt(2) - complex(0,1)*kap*TH1x3*TH3x4*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '-6*complex(0,1)*kk*lam1*TH1x4**3 - 6*alp1*complex(0,1)*kk*TH1x4*TH3x4**2 - 6*alp2*complex(0,1)*kk*TH1x4*TH3x4**2 - 6*alp1*complex(0,1)*kk*TH1x4*TH4x4**2 - 6*alp2*complex(0,1)*kk*TH1x4*TH4x4**2 - 6*alp1*complex(0,1)*TH1x4**2*TH3x4*vL - 6*alp2*complex(0,1)*TH1x4**2*TH3x4*vL - 6*complex(0,1)*lam3*TH3x4**3*vL - 6*complex(0,1)*lam4*TH3x4*TH4x4**2*vL - 6*alp1*complex(0,1)*TH1x4**2*TH4x4*vR - 6*alp2*complex(0,1)*TH1x4**2*TH4x4*vR - 6*complex(0,1)*lam4*TH3x4**2*TH4x4*vR - 6*complex(0,1)*lam3*TH4x4**3*vR - 3*complex(0,1)*kap*TH1x4*TH3x4*TH4x4*cmath.sqrt(2)',
                  order = {'QED':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '(-2*complex(0,1)*kk*lam1*TH1x1)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*tb**2*TH1x1)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*tb**2*TH1x1)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*TH1x1*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*TH1x1*tz**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x1*vL)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x1*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x1*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x1*tz**2*vL)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x1*vR)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x1*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x1*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x1*tz**2*vR)/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH4x1*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH1x1*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*TH3x1*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2)',
                  order = {'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '(-2*complex(0,1)*kk*lam1*TH1x2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*tb**2*TH1x2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*tb**2*TH1x2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*TH1x2*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*TH1x2*tz**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x2*vL)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x2*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x2*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x2*tz**2*vL)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x2*vR)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x2*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x2*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x2*tz**2*vR)/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH4x2*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH1x2*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*TH3x2*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2)',
                  order = {'QED':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '(-2*complex(0,1)*kk*lam1*TH1x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*tb**2*TH1x3)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*tb**2*TH1x3)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*TH1x3*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*TH1x3*tz**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x3*vL)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x3*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x3*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x3*tz**2*vL)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x3*vR)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x3*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x3*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x3*tz**2*vR)/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH4x3*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH1x3*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*TH3x3*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2)',
                  order = {'QED':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '(-2*complex(0,1)*kk*lam1*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*tb**2*TH1x4)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*tb**2*TH1x4)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*kk*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*kk*TH1x4*tz**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH3x4*vL)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH3x4*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*TH3x4*vL)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*TH3x4*tz**2*vL)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*TH4x4*vR)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*TH4x4*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*TH4x4*vR)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*TH4x4*tz**2*vR)/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH4x4*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*tb*TH1x4*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2) + (complex(0,1)*kap*TH3x4*tz*cmath.sqrt(2))/(1 + tb**2 + tz**2)',
                  order = {'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '-((complex(0,1)*TH3x1*yd1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '-((complex(0,1)*TH3x2*yd1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_428 = Coupling(name = 'GC_428',
                  value = '-((complex(0,1)*TH3x3*yd1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '-((complex(0,1)*TH3x4*yd1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '-((tb*yd1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '(tb*yd1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '-((complex(0,1)*TH3x1*yd2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '-((complex(0,1)*TH3x2*yd2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '-((complex(0,1)*TH3x3*yd2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '-((complex(0,1)*TH3x4*yd2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '-((tb*yd2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(tb*yd2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '-((complex(0,1)*TH3x1*yd3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '-((complex(0,1)*TH3x2*yd3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '-((complex(0,1)*TH3x3*yd3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '-((complex(0,1)*TH3x4*yd3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '-((tb*yd3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '(tb*yd3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '-((complex(0,1)*TH4x1*ydp1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '-((complex(0,1)*TH4x2*ydp1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '-((complex(0,1)*TH4x3*ydp1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '-((complex(0,1)*TH4x4*ydp1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '-((tz*ydp1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '(tz*ydp1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '-((complex(0,1)*TH4x1*ydp2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '-((complex(0,1)*TH4x2*ydp2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '-((complex(0,1)*TH4x3*ydp2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '-((complex(0,1)*TH4x4*ydp2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '-((tz*ydp2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '(tz*ydp2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '-((complex(0,1)*TH4x1*ydp3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-((complex(0,1)*TH4x2*ydp3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '-((complex(0,1)*TH4x3*ydp3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '-((complex(0,1)*TH4x4*ydp3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '-((tz*ydp3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '(tz*ydp3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '-((complex(0,1)*TH1x1*ye1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '-((complex(0,1)*TH1x2*ye1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '-((complex(0,1)*TH1x3*ye1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((complex(0,1)*TH1x4*ye1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '-(ye1x1/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_467 = Coupling(name = 'GC_467',
                  value = 'ye1x1/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '-((complex(0,1)*TH1x1*ye2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-((complex(0,1)*TH1x2*ye2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '-((complex(0,1)*TH1x3*ye2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '-((complex(0,1)*TH1x4*ye2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '-(ye2x2/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = 'ye2x2/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '-((complex(0,1)*TH1x1*ye3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-((complex(0,1)*TH1x2*ye3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '-((complex(0,1)*TH1x3*ye3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '-((complex(0,1)*TH1x4*ye3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '-(ye3x3/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_479 = Coupling(name = 'GC_479',
                  value = 'ye3x3/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '-((complex(0,1)*TH4x1*yn1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '-((complex(0,1)*TH4x2*yn1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '-((complex(0,1)*TH4x3*yn1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '-((complex(0,1)*TH4x4*yn1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '-((tz*yn1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '(tz*yn1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '-((complex(0,1)*TH4x1*yn2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '-((complex(0,1)*TH4x2*yn2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '-((complex(0,1)*TH4x3*yn2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-((complex(0,1)*TH4x4*yn2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '-((tz*yn2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '(tz*yn2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '-((complex(0,1)*TH4x1*yn3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '-((complex(0,1)*TH4x2*yn3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '-((complex(0,1)*TH4x3*yn3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '-((complex(0,1)*TH4x4*yn3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '-((tz*yn3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(tz*yn3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '-((complex(0,1)*TH3x1*ynu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '-((complex(0,1)*TH3x2*ynu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '-((complex(0,1)*TH3x3*ynu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '-((complex(0,1)*TH3x4*ynu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '-((tb*ynu1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(tb*ynu1x1)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '-((complex(0,1)*TH3x1*ynu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '-((complex(0,1)*TH3x2*ynu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '-((complex(0,1)*TH3x3*ynu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '-((complex(0,1)*TH3x4*ynu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '-((tb*ynu2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(tb*ynu2x2)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '-((complex(0,1)*TH3x1*ynu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '-((complex(0,1)*TH3x2*ynu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '-((complex(0,1)*TH3x3*ynu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '-((complex(0,1)*TH3x4*ynu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '-((tb*ynu3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '(tb*ynu3x3)/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '-((complex(0,1)*TH1x1*yu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '-((complex(0,1)*TH1x2*yu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '-((complex(0,1)*TH1x3*yu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '-((complex(0,1)*TH1x4*yu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '-(yu1x1/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_521 = Coupling(name = 'GC_521',
                  value = 'yu1x1/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '-((complex(0,1)*TH1x1*yu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '-((complex(0,1)*TH1x2*yu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '-((complex(0,1)*TH1x3*yu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '-((complex(0,1)*TH1x4*yu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '-(yu2x2/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_527 = Coupling(name = 'GC_527',
                  value = 'yu2x2/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '-((complex(0,1)*TH1x1*yu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '-((complex(0,1)*TH1x2*yu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '-((complex(0,1)*TH1x3*yu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '-((complex(0,1)*TH1x4*yu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '-(yu3x3/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2)))',
                  order = {'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = 'yu3x3/(cmath.sqrt(2)*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(complex(0,1)*gL*complexconjugate(CKM1x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(complex(0,1)*gL*complexconjugate(CKM1x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '(complex(0,1)*gL*complexconjugate(CKM1x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(complex(0,1)*gL*complexconjugate(CKM2x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '(complex(0,1)*gL*complexconjugate(CKM2x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '(complex(0,1)*gL*complexconjugate(CKM2x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '(complex(0,1)*gL*complexconjugate(CKM3x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '(complex(0,1)*gL*complexconjugate(CKM3x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '(complex(0,1)*gL*complexconjugate(CKM3x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp1x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp1x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp1x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp2x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp2x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp2x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp3x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp3x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '(complex(0,1)*gR*complexconjugate(CKMp3x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS1x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS1x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS1x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS2x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS2x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS2x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS3x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS3x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(complex(0,1)*gL*complexconjugate(PMNS3x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp1x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp1x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp1x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp2x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp2x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp2x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp3x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp3x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '(complex(0,1)*gR*complexconjugate(PMNSp3x3))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '-(gR*cmath.cos(beta))/2.',
                  order = {'QED':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '-(complex(0,1)*gR*cmath.cos(beta))/2.',
                  order = {'QED':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '(complex(0,1)*gR*cmath.cos(beta))/2.',
                  order = {'QED':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '-(ct*cw*gL*gR*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_574 = Coupling(name = 'GC_574',
                  value = '-(ct*cw*complex(0,1)*gL*gR*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_575 = Coupling(name = 'GC_575',
                  value = '(ct*cw*gL*gR*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_576 = Coupling(name = 'GC_576',
                  value = '-(complex(0,1)*I10b11*cmath.cos(beta))',
                  order = {'QED':1})

GC_577 = Coupling(name = 'GC_577',
                  value = '-(complex(0,1)*I10b12*cmath.cos(beta))',
                  order = {'QED':1})

GC_578 = Coupling(name = 'GC_578',
                  value = '-(complex(0,1)*I10b13*cmath.cos(beta))',
                  order = {'QED':1})

GC_579 = Coupling(name = 'GC_579',
                  value = '-(complex(0,1)*I10b21*cmath.cos(beta))',
                  order = {'QED':1})

GC_580 = Coupling(name = 'GC_580',
                  value = '-(complex(0,1)*I10b22*cmath.cos(beta))',
                  order = {'QED':1})

GC_581 = Coupling(name = 'GC_581',
                  value = '-(complex(0,1)*I10b23*cmath.cos(beta))',
                  order = {'QED':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '-(complex(0,1)*I10b31*cmath.cos(beta))',
                  order = {'QED':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '-(complex(0,1)*I10b32*cmath.cos(beta))',
                  order = {'QED':1})

GC_584 = Coupling(name = 'GC_584',
                  value = '-(complex(0,1)*I10b33*cmath.cos(beta))',
                  order = {'QED':1})

GC_585 = Coupling(name = 'GC_585',
                  value = 'complex(0,1)*I13b11*cmath.cos(beta)',
                  order = {'QED':1})

GC_586 = Coupling(name = 'GC_586',
                  value = 'complex(0,1)*I13b12*cmath.cos(beta)',
                  order = {'QED':1})

GC_587 = Coupling(name = 'GC_587',
                  value = 'complex(0,1)*I13b13*cmath.cos(beta)',
                  order = {'QED':1})

GC_588 = Coupling(name = 'GC_588',
                  value = 'complex(0,1)*I13b21*cmath.cos(beta)',
                  order = {'QED':1})

GC_589 = Coupling(name = 'GC_589',
                  value = 'complex(0,1)*I13b22*cmath.cos(beta)',
                  order = {'QED':1})

GC_590 = Coupling(name = 'GC_590',
                  value = 'complex(0,1)*I13b23*cmath.cos(beta)',
                  order = {'QED':1})

GC_591 = Coupling(name = 'GC_591',
                  value = 'complex(0,1)*I13b31*cmath.cos(beta)',
                  order = {'QED':1})

GC_592 = Coupling(name = 'GC_592',
                  value = 'complex(0,1)*I13b32*cmath.cos(beta)',
                  order = {'QED':1})

GC_593 = Coupling(name = 'GC_593',
                  value = 'complex(0,1)*I13b33*cmath.cos(beta)',
                  order = {'QED':1})

GC_594 = Coupling(name = 'GC_594',
                  value = 'complex(0,1)*I2b11*cmath.cos(beta)',
                  order = {'QED':1})

GC_595 = Coupling(name = 'GC_595',
                  value = 'complex(0,1)*I2b12*cmath.cos(beta)',
                  order = {'QED':1})

GC_596 = Coupling(name = 'GC_596',
                  value = 'complex(0,1)*I2b13*cmath.cos(beta)',
                  order = {'QED':1})

GC_597 = Coupling(name = 'GC_597',
                  value = 'complex(0,1)*I2b21*cmath.cos(beta)',
                  order = {'QED':1})

GC_598 = Coupling(name = 'GC_598',
                  value = 'complex(0,1)*I2b22*cmath.cos(beta)',
                  order = {'QED':1})

GC_599 = Coupling(name = 'GC_599',
                  value = 'complex(0,1)*I2b23*cmath.cos(beta)',
                  order = {'QED':1})

GC_600 = Coupling(name = 'GC_600',
                  value = 'complex(0,1)*I2b31*cmath.cos(beta)',
                  order = {'QED':1})

GC_601 = Coupling(name = 'GC_601',
                  value = 'complex(0,1)*I2b32*cmath.cos(beta)',
                  order = {'QED':1})

GC_602 = Coupling(name = 'GC_602',
                  value = 'complex(0,1)*I2b33*cmath.cos(beta)',
                  order = {'QED':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '-(complex(0,1)*I6b11*cmath.cos(beta))',
                  order = {'QED':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '-(complex(0,1)*I6b12*cmath.cos(beta))',
                  order = {'QED':1})

GC_605 = Coupling(name = 'GC_605',
                  value = '-(complex(0,1)*I6b13*cmath.cos(beta))',
                  order = {'QED':1})

GC_606 = Coupling(name = 'GC_606',
                  value = '-(complex(0,1)*I6b21*cmath.cos(beta))',
                  order = {'QED':1})

GC_607 = Coupling(name = 'GC_607',
                  value = '-(complex(0,1)*I6b22*cmath.cos(beta))',
                  order = {'QED':1})

GC_608 = Coupling(name = 'GC_608',
                  value = '-(complex(0,1)*I6b23*cmath.cos(beta))',
                  order = {'QED':1})

GC_609 = Coupling(name = 'GC_609',
                  value = '-(complex(0,1)*I6b31*cmath.cos(beta))',
                  order = {'QED':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(complex(0,1)*I6b32*cmath.cos(beta))',
                  order = {'QED':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '-(complex(0,1)*I6b33*cmath.cos(beta))',
                  order = {'QED':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '-(cw*gL*gR*st*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '(cw*complex(0,1)*gL*gR*st*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '(cw*gL*gR*st*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '-(gL*gR*sw*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '-(complex(0,1)*gL*gR*sw*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '(gL*gR*sw*cmath.cos(beta))/2.',
                  order = {'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '(complex(0,1)*gR**2*cmath.cos(beta)**2)/2.',
                  order = {'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '-(complex(0,1)*gL*cmath.cos(zeta))/2.',
                  order = {'QED':1})

GC_620 = Coupling(name = 'GC_620',
                  value = '(complex(0,1)*gL*cmath.cos(zeta))/2.',
                  order = {'QED':1})

GC_621 = Coupling(name = 'GC_621',
                  value = '(gL*cmath.cos(zeta))/2.',
                  order = {'QED':1})

GC_622 = Coupling(name = 'GC_622',
                  value = 'complex(0,1)*I16b11*cmath.cos(zeta)',
                  order = {'QED':1})

GC_623 = Coupling(name = 'GC_623',
                  value = 'complex(0,1)*I16b12*cmath.cos(zeta)',
                  order = {'QED':1})

GC_624 = Coupling(name = 'GC_624',
                  value = 'complex(0,1)*I16b13*cmath.cos(zeta)',
                  order = {'QED':1})

GC_625 = Coupling(name = 'GC_625',
                  value = 'complex(0,1)*I16b21*cmath.cos(zeta)',
                  order = {'QED':1})

GC_626 = Coupling(name = 'GC_626',
                  value = 'complex(0,1)*I16b22*cmath.cos(zeta)',
                  order = {'QED':1})

GC_627 = Coupling(name = 'GC_627',
                  value = 'complex(0,1)*I16b23*cmath.cos(zeta)',
                  order = {'QED':1})

GC_628 = Coupling(name = 'GC_628',
                  value = 'complex(0,1)*I16b31*cmath.cos(zeta)',
                  order = {'QED':1})

GC_629 = Coupling(name = 'GC_629',
                  value = 'complex(0,1)*I16b32*cmath.cos(zeta)',
                  order = {'QED':1})

GC_630 = Coupling(name = 'GC_630',
                  value = 'complex(0,1)*I16b33*cmath.cos(zeta)',
                  order = {'QED':1})

GC_631 = Coupling(name = 'GC_631',
                  value = '-(complex(0,1)*I18b11*cmath.cos(zeta))',
                  order = {'QED':1})

GC_632 = Coupling(name = 'GC_632',
                  value = '-(complex(0,1)*I18b12*cmath.cos(zeta))',
                  order = {'QED':1})

GC_633 = Coupling(name = 'GC_633',
                  value = '-(complex(0,1)*I18b13*cmath.cos(zeta))',
                  order = {'QED':1})

GC_634 = Coupling(name = 'GC_634',
                  value = '-(complex(0,1)*I18b21*cmath.cos(zeta))',
                  order = {'QED':1})

GC_635 = Coupling(name = 'GC_635',
                  value = '-(complex(0,1)*I18b22*cmath.cos(zeta))',
                  order = {'QED':1})

GC_636 = Coupling(name = 'GC_636',
                  value = '-(complex(0,1)*I18b23*cmath.cos(zeta))',
                  order = {'QED':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '-(complex(0,1)*I18b31*cmath.cos(zeta))',
                  order = {'QED':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(complex(0,1)*I18b32*cmath.cos(zeta))',
                  order = {'QED':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '-(complex(0,1)*I18b33*cmath.cos(zeta))',
                  order = {'QED':1})

GC_640 = Coupling(name = 'GC_640',
                  value = 'complex(0,1)*I4b11*cmath.cos(zeta)',
                  order = {'QED':1})

GC_641 = Coupling(name = 'GC_641',
                  value = 'complex(0,1)*I4b12*cmath.cos(zeta)',
                  order = {'QED':1})

GC_642 = Coupling(name = 'GC_642',
                  value = 'complex(0,1)*I4b13*cmath.cos(zeta)',
                  order = {'QED':1})

GC_643 = Coupling(name = 'GC_643',
                  value = 'complex(0,1)*I4b21*cmath.cos(zeta)',
                  order = {'QED':1})

GC_644 = Coupling(name = 'GC_644',
                  value = 'complex(0,1)*I4b22*cmath.cos(zeta)',
                  order = {'QED':1})

GC_645 = Coupling(name = 'GC_645',
                  value = 'complex(0,1)*I4b23*cmath.cos(zeta)',
                  order = {'QED':1})

GC_646 = Coupling(name = 'GC_646',
                  value = 'complex(0,1)*I4b31*cmath.cos(zeta)',
                  order = {'QED':1})

GC_647 = Coupling(name = 'GC_647',
                  value = 'complex(0,1)*I4b32*cmath.cos(zeta)',
                  order = {'QED':1})

GC_648 = Coupling(name = 'GC_648',
                  value = 'complex(0,1)*I4b33*cmath.cos(zeta)',
                  order = {'QED':1})

GC_649 = Coupling(name = 'GC_649',
                  value = '-(complex(0,1)*I8b11*cmath.cos(zeta))',
                  order = {'QED':1})

GC_650 = Coupling(name = 'GC_650',
                  value = '-(complex(0,1)*I8b12*cmath.cos(zeta))',
                  order = {'QED':1})

GC_651 = Coupling(name = 'GC_651',
                  value = '-(complex(0,1)*I8b13*cmath.cos(zeta))',
                  order = {'QED':1})

GC_652 = Coupling(name = 'GC_652',
                  value = '-(complex(0,1)*I8b21*cmath.cos(zeta))',
                  order = {'QED':1})

GC_653 = Coupling(name = 'GC_653',
                  value = '-(complex(0,1)*I8b22*cmath.cos(zeta))',
                  order = {'QED':1})

GC_654 = Coupling(name = 'GC_654',
                  value = '-(complex(0,1)*I8b23*cmath.cos(zeta))',
                  order = {'QED':1})

GC_655 = Coupling(name = 'GC_655',
                  value = '-(complex(0,1)*I8b31*cmath.cos(zeta))',
                  order = {'QED':1})

GC_656 = Coupling(name = 'GC_656',
                  value = '-(complex(0,1)*I8b32*cmath.cos(zeta))',
                  order = {'QED':1})

GC_657 = Coupling(name = 'GC_657',
                  value = '-(complex(0,1)*I8b33*cmath.cos(zeta))',
                  order = {'QED':1})

GC_658 = Coupling(name = 'GC_658',
                  value = '-(cw*gL*gR*sph*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '-(cw*complex(0,1)*gL*gR*sph*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cw*gL*gR*sph*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_661 = Coupling(name = 'GC_661',
                  value = '-(complex(0,1)*gL*gR*cmath.cos(beta)*cmath.cos(zeta))',
                  order = {'QED':2})

GC_662 = Coupling(name = 'GC_662',
                  value = '(complex(0,1)*gL**2*cmath.cos(zeta)**2)/2.',
                  order = {'QED':2})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cph*gL*gR*st*cmath.cos(zeta))/2. - (ct*gL*gR*sph*sw*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_664 = Coupling(name = 'GC_664',
                  value = '-(cph*complex(0,1)*gL*gR*st*cmath.cos(zeta))/2. + (ct*complex(0,1)*gL*gR*sph*sw*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_665 = Coupling(name = 'GC_665',
                  value = '-(cph*gL*gR*st*cmath.cos(zeta))/2. + (ct*gL*gR*sph*sw*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_666 = Coupling(name = 'GC_666',
                  value = '-(cph*ct*gL*gR*cmath.cos(zeta))/2. - (gL*gR*sph*st*sw*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '-(cph*ct*complex(0,1)*gL*gR*cmath.cos(zeta))/2. - (complex(0,1)*gL*gR*sph*st*sw*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '(cph*ct*gL*gR*cmath.cos(zeta))/2. + (gL*gR*sph*st*sw*cmath.cos(zeta))/2.',
                  order = {'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '-(complex(0,1)*I11b11*cmath.sin(beta))',
                  order = {'QED':1})

GC_670 = Coupling(name = 'GC_670',
                  value = '-(complex(0,1)*I11b12*cmath.sin(beta))',
                  order = {'QED':1})

GC_671 = Coupling(name = 'GC_671',
                  value = '-(complex(0,1)*I11b13*cmath.sin(beta))',
                  order = {'QED':1})

GC_672 = Coupling(name = 'GC_672',
                  value = '-(complex(0,1)*I11b21*cmath.sin(beta))',
                  order = {'QED':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '-(complex(0,1)*I11b22*cmath.sin(beta))',
                  order = {'QED':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '-(complex(0,1)*I11b23*cmath.sin(beta))',
                  order = {'QED':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '-(complex(0,1)*I11b31*cmath.sin(beta))',
                  order = {'QED':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '-(complex(0,1)*I11b32*cmath.sin(beta))',
                  order = {'QED':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '-(complex(0,1)*I11b33*cmath.sin(beta))',
                  order = {'QED':1})

GC_678 = Coupling(name = 'GC_678',
                  value = 'complex(0,1)*I12b11*cmath.sin(beta)',
                  order = {'QED':1})

GC_679 = Coupling(name = 'GC_679',
                  value = 'complex(0,1)*I12b12*cmath.sin(beta)',
                  order = {'QED':1})

GC_680 = Coupling(name = 'GC_680',
                  value = 'complex(0,1)*I12b13*cmath.sin(beta)',
                  order = {'QED':1})

GC_681 = Coupling(name = 'GC_681',
                  value = 'complex(0,1)*I12b21*cmath.sin(beta)',
                  order = {'QED':1})

GC_682 = Coupling(name = 'GC_682',
                  value = 'complex(0,1)*I12b22*cmath.sin(beta)',
                  order = {'QED':1})

GC_683 = Coupling(name = 'GC_683',
                  value = 'complex(0,1)*I12b23*cmath.sin(beta)',
                  order = {'QED':1})

GC_684 = Coupling(name = 'GC_684',
                  value = 'complex(0,1)*I12b31*cmath.sin(beta)',
                  order = {'QED':1})

GC_685 = Coupling(name = 'GC_685',
                  value = 'complex(0,1)*I12b32*cmath.sin(beta)',
                  order = {'QED':1})

GC_686 = Coupling(name = 'GC_686',
                  value = 'complex(0,1)*I12b33*cmath.sin(beta)',
                  order = {'QED':1})

GC_687 = Coupling(name = 'GC_687',
                  value = 'complex(0,1)*I1b11*cmath.sin(beta)',
                  order = {'QED':1})

GC_688 = Coupling(name = 'GC_688',
                  value = 'complex(0,1)*I1b12*cmath.sin(beta)',
                  order = {'QED':1})

GC_689 = Coupling(name = 'GC_689',
                  value = 'complex(0,1)*I1b13*cmath.sin(beta)',
                  order = {'QED':1})

GC_690 = Coupling(name = 'GC_690',
                  value = 'complex(0,1)*I1b21*cmath.sin(beta)',
                  order = {'QED':1})

GC_691 = Coupling(name = 'GC_691',
                  value = 'complex(0,1)*I1b22*cmath.sin(beta)',
                  order = {'QED':1})

GC_692 = Coupling(name = 'GC_692',
                  value = 'complex(0,1)*I1b23*cmath.sin(beta)',
                  order = {'QED':1})

GC_693 = Coupling(name = 'GC_693',
                  value = 'complex(0,1)*I1b31*cmath.sin(beta)',
                  order = {'QED':1})

GC_694 = Coupling(name = 'GC_694',
                  value = 'complex(0,1)*I1b32*cmath.sin(beta)',
                  order = {'QED':1})

GC_695 = Coupling(name = 'GC_695',
                  value = 'complex(0,1)*I1b33*cmath.sin(beta)',
                  order = {'QED':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '-(complex(0,1)*I7b11*cmath.sin(beta))',
                  order = {'QED':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '-(complex(0,1)*I7b12*cmath.sin(beta))',
                  order = {'QED':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '-(complex(0,1)*I7b13*cmath.sin(beta))',
                  order = {'QED':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '-(complex(0,1)*I7b21*cmath.sin(beta))',
                  order = {'QED':1})

GC_700 = Coupling(name = 'GC_700',
                  value = '-(complex(0,1)*I7b22*cmath.sin(beta))',
                  order = {'QED':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '-(complex(0,1)*I7b23*cmath.sin(beta))',
                  order = {'QED':1})

GC_702 = Coupling(name = 'GC_702',
                  value = '-(complex(0,1)*I7b31*cmath.sin(beta))',
                  order = {'QED':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '-(complex(0,1)*I7b32*cmath.sin(beta))',
                  order = {'QED':1})

GC_704 = Coupling(name = 'GC_704',
                  value = '-(complex(0,1)*I7b33*cmath.sin(beta))',
                  order = {'QED':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '(complex(0,1)*gL*TH1x1*cmath.cos(beta))/2. - (complex(0,1)*gL*TH3x1*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_706 = Coupling(name = 'GC_706',
                  value = '-(complex(0,1)*gL*TH1x1*cmath.cos(beta))/2. + (complex(0,1)*gL*TH3x1*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '(cw*complex(0,1)*gL*gR*sph*TH1x1*cmath.cos(beta))/2. - (cph*cw*complex(0,1)*gBL*gL*TH3x1*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '(cph*complex(0,1)*gL*gR*st*TH1x1*cmath.cos(beta))/2. - (ct*complex(0,1)*gL*gR*sph*sw*TH1x1*cmath.cos(beta))/2. + (complex(0,1)*gBL*gL*sph*st*TH3x1*cmath.sin(beta))/2. + (cph*ct*complex(0,1)*gBL*gL*sw*TH3x1*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_709 = Coupling(name = 'GC_709',
                  value = '(cph*ct*complex(0,1)*gL*gR*TH1x1*cmath.cos(beta))/2. + (complex(0,1)*gL*gR*sph*st*sw*TH1x1*cmath.cos(beta))/2. + (ct*complex(0,1)*gBL*gL*sph*TH3x1*cmath.sin(beta))/2. - (cph*complex(0,1)*gBL*gL*st*sw*TH3x1*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '(complex(0,1)*gL*TH1x2*cmath.cos(beta))/2. - (complex(0,1)*gL*TH3x2*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '-(complex(0,1)*gL*TH1x2*cmath.cos(beta))/2. + (complex(0,1)*gL*TH3x2*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_712 = Coupling(name = 'GC_712',
                  value = '(cw*complex(0,1)*gL*gR*sph*TH1x2*cmath.cos(beta))/2. - (cph*cw*complex(0,1)*gBL*gL*TH3x2*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '(cph*complex(0,1)*gL*gR*st*TH1x2*cmath.cos(beta))/2. - (ct*complex(0,1)*gL*gR*sph*sw*TH1x2*cmath.cos(beta))/2. + (complex(0,1)*gBL*gL*sph*st*TH3x2*cmath.sin(beta))/2. + (cph*ct*complex(0,1)*gBL*gL*sw*TH3x2*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '(cph*ct*complex(0,1)*gL*gR*TH1x2*cmath.cos(beta))/2. + (complex(0,1)*gL*gR*sph*st*sw*TH1x2*cmath.cos(beta))/2. + (ct*complex(0,1)*gBL*gL*sph*TH3x2*cmath.sin(beta))/2. - (cph*complex(0,1)*gBL*gL*st*sw*TH3x2*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '(complex(0,1)*gL*TH1x3*cmath.cos(beta))/2. - (complex(0,1)*gL*TH3x3*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_716 = Coupling(name = 'GC_716',
                  value = '-(complex(0,1)*gL*TH1x3*cmath.cos(beta))/2. + (complex(0,1)*gL*TH3x3*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '(cw*complex(0,1)*gL*gR*sph*TH1x3*cmath.cos(beta))/2. - (cph*cw*complex(0,1)*gBL*gL*TH3x3*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '(cph*complex(0,1)*gL*gR*st*TH1x3*cmath.cos(beta))/2. - (ct*complex(0,1)*gL*gR*sph*sw*TH1x3*cmath.cos(beta))/2. + (complex(0,1)*gBL*gL*sph*st*TH3x3*cmath.sin(beta))/2. + (cph*ct*complex(0,1)*gBL*gL*sw*TH3x3*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(cph*ct*complex(0,1)*gL*gR*TH1x3*cmath.cos(beta))/2. + (complex(0,1)*gL*gR*sph*st*sw*TH1x3*cmath.cos(beta))/2. + (ct*complex(0,1)*gBL*gL*sph*TH3x3*cmath.sin(beta))/2. - (cph*complex(0,1)*gBL*gL*st*sw*TH3x3*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '(complex(0,1)*gL*TH1x4*cmath.cos(beta))/2. - (complex(0,1)*gL*TH3x4*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '-(complex(0,1)*gL*TH1x4*cmath.cos(beta))/2. + (complex(0,1)*gL*TH3x4*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '(cw*complex(0,1)*gL*gR*sph*TH1x4*cmath.cos(beta))/2. - (cph*cw*complex(0,1)*gBL*gL*TH3x4*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(cph*complex(0,1)*gL*gR*st*TH1x4*cmath.cos(beta))/2. - (ct*complex(0,1)*gL*gR*sph*sw*TH1x4*cmath.cos(beta))/2. + (complex(0,1)*gBL*gL*sph*st*TH3x4*cmath.sin(beta))/2. + (cph*ct*complex(0,1)*gBL*gL*sw*TH3x4*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '(cph*ct*complex(0,1)*gL*gR*TH1x4*cmath.cos(beta))/2. + (complex(0,1)*gL*gR*sph*st*sw*TH1x4*cmath.cos(beta))/2. + (ct*complex(0,1)*gBL*gL*sph*TH3x4*cmath.sin(beta))/2. - (cph*complex(0,1)*gBL*gL*st*sw*TH3x4*cmath.sin(beta))/2.',
                  order = {'QED':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '(gL*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gL*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_726 = Coupling(name = 'GC_726',
                  value = '-(cw*gL*gR*sph*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*cw*gBL*gL*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '(cw*gL*gR*sph*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*cw*gBL*gL*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '(cph*gL*gR*st*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gL*gR*sph*sw*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gBL*gL*sph*st*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gBL*gL*sw*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_729 = Coupling(name = 'GC_729',
                  value = '-(cph*gL*gR*st*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gL*gR*sph*sw*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gBL*gL*sph*st*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*ct*gBL*gL*sw*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_730 = Coupling(name = 'GC_730',
                  value = '-(cph*ct*gL*gR*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gL*gR*sph*st*sw*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gBL*gL*sph*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gBL*gL*st*sw*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_731 = Coupling(name = 'GC_731',
                  value = '(cph*ct*gL*gR*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gL*gR*sph*st*sw*cmath.cos(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gBL*gL*sph*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gBL*gL*st*sw*tb*cmath.sin(beta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_732 = Coupling(name = 'GC_732',
                  value = '(cw*complex(0,1)*gL*gR*kk*sph*cmath.cos(beta))/2. - (cph*cw*complex(0,1)*gBL*gL*vL*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '(cph*complex(0,1)*gL*gR*kk*st*cmath.cos(beta))/2. - (ct*complex(0,1)*gL*gR*kk*sph*sw*cmath.cos(beta))/2. + (complex(0,1)*gBL*gL*sph*st*vL*cmath.sin(beta))/2. + (cph*ct*complex(0,1)*gBL*gL*sw*vL*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '(cph*ct*complex(0,1)*gL*gR*kk*cmath.cos(beta))/2. + (complex(0,1)*gL*gR*kk*sph*st*sw*cmath.cos(beta))/2. + (ct*complex(0,1)*gBL*gL*sph*vL*cmath.sin(beta))/2. - (cph*complex(0,1)*gBL*gL*st*sw*vL*cmath.sin(beta))/2.',
                  order = {'QED':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '-2*complex(0,1)*lam1*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*cmath.sin(beta)**2 - 2*alp2*complex(0,1)*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '(complex(0,1)*gL**2*cmath.cos(beta)**2)/2. + (complex(0,1)*gL**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_737 = Coupling(name = 'GC_737',
                  value = '-(ct*cw*complex(0,1)*gL*cmath.cos(beta)**2)/2. - (cph*complex(0,1)*gR*st*cmath.cos(beta)**2)/2. + (ct*complex(0,1)*gR*sph*sw*cmath.cos(beta)**2)/2. - (ct*cw*complex(0,1)*gL*cmath.sin(beta)**2)/2. + (complex(0,1)*gBL*sph*st*cmath.sin(beta)**2)/2. + (cph*ct*complex(0,1)*gBL*sw*cmath.sin(beta)**2)/2.',
                  order = {'QED':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '-(cw*complex(0,1)*gR*sph*cmath.cos(beta)**2)/2. - (complex(0,1)*gL*sw*cmath.cos(beta)**2)/2. - (cph*cw*complex(0,1)*gBL*cmath.sin(beta)**2)/2. - (complex(0,1)*gL*sw*cmath.sin(beta)**2)/2.',
                  order = {'QED':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '(cw*complex(0,1)*gR*sph*cmath.cos(beta)**2)/2. + (complex(0,1)*gL*sw*cmath.cos(beta)**2)/2. + (cph*cw*complex(0,1)*gBL*cmath.sin(beta)**2)/2. + (complex(0,1)*gL*sw*cmath.sin(beta)**2)/2.',
                  order = {'QED':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '-(cph*ct*complex(0,1)*gR*cmath.cos(beta)**2)/2. + (cw*complex(0,1)*gL*st*cmath.cos(beta)**2)/2. - (complex(0,1)*gR*sph*st*sw*cmath.cos(beta)**2)/2. + (ct*complex(0,1)*gBL*sph*cmath.sin(beta)**2)/2. + (cw*complex(0,1)*gL*st*cmath.sin(beta)**2)/2. - (cph*complex(0,1)*gBL*st*sw*cmath.sin(beta)**2)/2.',
                  order = {'QED':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*cmath.cos(beta)**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*cmath.cos(beta)**2 + (cph**2*complex(0,1)*gR**2*st**2*cmath.cos(beta)**2)/2. - ct**2*cw*complex(0,1)*gL*gR*sph*sw*cmath.cos(beta)**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*cmath.cos(beta)**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*cmath.cos(beta)**2)/2. + (ct**2*cw**2*complex(0,1)*gL**2*cmath.sin(beta)**2)/2. - ct*cw*complex(0,1)*gBL*gL*sph*st*cmath.sin(beta)**2 + (complex(0,1)*gBL**2*sph**2*st**2*cmath.sin(beta)**2)/2. - cph*ct**2*cw*complex(0,1)*gBL*gL*sw*cmath.sin(beta)**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*cmath.sin(beta)**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_742 = Coupling(name = 'GC_742',
                  value = '(ct*cw**2*complex(0,1)*gL*gR*sph*cmath.cos(beta)**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*cmath.cos(beta)**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*cmath.cos(beta)**2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*cmath.cos(beta)**2)/2. + (cph*complex(0,1)*gL*gR*st*sw*cmath.cos(beta)**2)/2. - (ct*complex(0,1)*gL*gR*sph*sw**2*cmath.cos(beta)**2)/2. + (cph*ct*cw**2*complex(0,1)*gBL*gL*cmath.sin(beta)**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*cmath.sin(beta)**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*cmath.sin(beta)**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*cmath.sin(beta)**2)/2. - (complex(0,1)*gBL*gL*sph*st*sw*cmath.sin(beta)**2)/2. - (cph*ct*complex(0,1)*gBL*gL*sw**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_743 = Coupling(name = 'GC_743',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*cmath.cos(beta)**2)/2. + cw*complex(0,1)*gL*gR*sph*sw*cmath.cos(beta)**2 + (complex(0,1)*gL**2*sw**2*cmath.cos(beta)**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*cmath.sin(beta)**2)/2. + cph*cw*complex(0,1)*gBL*gL*sw*cmath.sin(beta)**2 + (complex(0,1)*gL**2*sw**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_744 = Coupling(name = 'GC_744',
                  value = '(cph*ct**2*cw*complex(0,1)*gL*gR*cmath.cos(beta)**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*cmath.cos(beta)**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*cmath.cos(beta)**2)/2. - (cph*cw*complex(0,1)*gL*gR*st**2*cmath.cos(beta)**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*cmath.cos(beta)**2)/2. + ct*cw*complex(0,1)*gL*gR*sph*st*sw*cmath.cos(beta)**2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*cmath.cos(beta)**2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*cmath.cos(beta)**2)/2. - (ct**2*cw*complex(0,1)*gBL*gL*sph*cmath.sin(beta)**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*cmath.sin(beta)**2)/2. + (ct*complex(0,1)*gBL**2*sph**2*st*cmath.sin(beta)**2)/2. + (cw*complex(0,1)*gBL*gL*sph*st**2*cmath.sin(beta)**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*cmath.sin(beta)**2)/2. + cph*ct*cw*complex(0,1)*gBL*gL*st*sw*cmath.sin(beta)**2 - (cph*complex(0,1)*gBL**2*sph*st**2*sw*cmath.sin(beta)**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_745 = Coupling(name = 'GC_745',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*cmath.cos(beta)**2)/2. - (cw**2*complex(0,1)*gL*gR*sph*st*cmath.cos(beta)**2)/2. + (cph*ct*complex(0,1)*gL*gR*sw*cmath.cos(beta)**2)/2. - (cw*complex(0,1)*gL**2*st*sw*cmath.cos(beta)**2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*cmath.cos(beta)**2)/2. + (complex(0,1)*gL*gR*sph*st*sw**2*cmath.cos(beta)**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*cmath.sin(beta)**2)/2. - (cph*cw**2*complex(0,1)*gBL*gL*st*cmath.sin(beta)**2)/2. - (ct*complex(0,1)*gBL*gL*sph*sw*cmath.sin(beta)**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*cmath.sin(beta)**2)/2. - (cw*complex(0,1)*gL**2*st*sw*cmath.sin(beta)**2)/2. + (cph*complex(0,1)*gBL*gL*st*sw**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_746 = Coupling(name = 'GC_746',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*cmath.cos(beta)**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*cmath.cos(beta)**2 + (cw**2*complex(0,1)*gL**2*st**2*cmath.cos(beta)**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*cmath.cos(beta)**2 - cw*complex(0,1)*gL*gR*sph*st**2*sw*cmath.cos(beta)**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*cmath.cos(beta)**2)/2. + (ct**2*complex(0,1)*gBL**2*sph**2*cmath.sin(beta)**2)/2. + ct*cw*complex(0,1)*gBL*gL*sph*st*cmath.sin(beta)**2 + (cw**2*complex(0,1)*gL**2*st**2*cmath.sin(beta)**2)/2. - cph*ct*complex(0,1)*gBL**2*sph*st*sw*cmath.sin(beta)**2 - cph*cw*complex(0,1)*gBL*gL*st**2*sw*cmath.sin(beta)**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*cmath.sin(beta)**2)/2.',
                  order = {'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '-2*complex(0,1)*lam1*TH1x1**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x1**2*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x1**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x1**2*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x1**2*cmath.cos(beta)**2 + 4*alp2*complex(0,1)*TH1x1*TH3x1*cmath.cos(beta)*cmath.sin(beta) - 4*alp3*complex(0,1)*TH1x1*TH3x1*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x1**2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x1**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x1**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x1**2*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x1*TH3x2*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x1*TH3x2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x1*TH4x2*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x1*TH4x2*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*TH1x2*TH3x1*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x2*TH3x1*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x1*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x1*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x1*TH1x2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x1*TH1x2*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x1*TH3x2*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x1*TH4x2*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_749 = Coupling(name = 'GC_749',
                  value = '-2*complex(0,1)*lam1*cmath.cos(beta)**2 - 2*complex(0,1)*lam1*TH1x2**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x2**2*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x2**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x2**2*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x2**2*cmath.cos(beta)**2 + 4*alp2*complex(0,1)*TH1x2*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 4*alp3*complex(0,1)*TH1x2*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*cmath.sin(beta)**2 - 2*alp2*complex(0,1)*cmath.sin(beta)**2 - 2*alp1*complex(0,1)*TH1x2**2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x2**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x2**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x2**2*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_750 = Coupling(name = 'GC_750',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x3*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x1*TH3x3*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x1*TH3x3*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x1*TH4x3*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x1*TH4x3*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*TH1x3*TH3x1*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x3*TH3x1*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x1*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x1*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x1*TH1x3*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x1*TH1x3*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x1*TH3x3*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x1*TH4x3*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x3*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x2*TH3x3*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x2*TH3x3*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x2*TH4x3*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x2*TH4x3*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*TH1x3*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x3*TH3x2*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x2*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x2*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x2*TH1x3*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x2*TH1x3*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x2*TH3x3*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x2*TH4x3*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_752 = Coupling(name = 'GC_752',
                  value = '-2*complex(0,1)*lam1*TH1x3**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x3**2*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x3**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x3**2*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x3**2*cmath.cos(beta)**2 + 4*alp2*complex(0,1)*TH1x3*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 4*alp3*complex(0,1)*TH1x3*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x3**2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x3**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x3**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x3**2*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_753 = Coupling(name = 'GC_753',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x1*TH3x4*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x1*TH3x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x1*TH4x4*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x1*TH4x4*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*TH1x4*TH3x1*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x4*TH3x1*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x1*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x1*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x1*TH1x4*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x1*TH1x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x1*TH3x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x1*TH4x4*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_754 = Coupling(name = 'GC_754',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x2*TH3x4*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x2*TH3x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x2*TH4x4*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x2*TH4x4*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*TH1x4*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x4*TH3x2*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x2*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x2*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x2*TH1x4*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x2*TH1x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x2*TH3x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x2*TH4x4*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_755 = Coupling(name = 'GC_755',
                  value = '-2*complex(0,1)*lam1*TH1x3*TH1x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x3*TH3x4*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x3*TH3x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x3*TH4x4*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x3*TH4x4*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*TH1x4*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x4*TH3x3*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x3*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x3*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x3*TH1x4*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x3*TH1x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x3*TH3x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x3*TH4x4*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_756 = Coupling(name = 'GC_756',
                  value = '-2*complex(0,1)*lam1*TH1x4**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x4**2*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x4**2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x4**2*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x4**2*cmath.cos(beta)**2 + 4*alp2*complex(0,1)*TH1x4*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 4*alp3*complex(0,1)*TH1x4*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp1*complex(0,1)*TH1x4**2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*TH1x4**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x4**2*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x4**2*cmath.sin(beta)**2',
                  order = {'QED':2})

GC_757 = Coupling(name = 'GC_757',
                  value = '(-2*complex(0,1)*lam1*cmath.cos(beta)**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*cmath.cos(beta)**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*tb**2*cmath.cos(beta)**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tz**2*cmath.cos(beta)**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tz**2*cmath.cos(beta)**2)/(1 + tb**2 + tz**2) - (4*alp2*complex(0,1)*tb*cmath.cos(beta)*cmath.sin(beta))/(1 + tb**2 + tz**2) + (4*alp3*complex(0,1)*tb*cmath.cos(beta)*cmath.sin(beta))/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*cmath.sin(beta)**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*cmath.sin(beta)**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tb**2*cmath.sin(beta)**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tz**2*cmath.sin(beta)**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_758 = Coupling(name = 'GC_758',
                  value = '-2*complex(0,1)*kk*lam1*TH1x1*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x1*vL*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x1*vL*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x1*vR*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x1*vR*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*kk*TH3x1*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*kk*TH3x1*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x1*vL*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x1*vL*cmath.cos(beta)*cmath.sin(beta) + complex(0,1)*kap*TH4x1*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta) - 2*alp1*complex(0,1)*kk*TH1x1*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*kk*TH1x1*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x1*vL*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x1*vR*cmath.sin(beta)**2',
                  order = {'QED':1})

GC_759 = Coupling(name = 'GC_759',
                  value = '-2*complex(0,1)*kk*lam1*TH1x2*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x2*vL*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x2*vL*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x2*vR*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x2*vR*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*kk*TH3x2*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*kk*TH3x2*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x2*vL*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x2*vL*cmath.cos(beta)*cmath.sin(beta) + complex(0,1)*kap*TH4x2*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta) - 2*alp1*complex(0,1)*kk*TH1x2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*kk*TH1x2*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x2*vL*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x2*vR*cmath.sin(beta)**2',
                  order = {'QED':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '-2*complex(0,1)*kk*lam1*TH1x3*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x3*vL*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x3*vL*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x3*vR*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x3*vR*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*kk*TH3x3*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*kk*TH3x3*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x3*vL*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x3*vL*cmath.cos(beta)*cmath.sin(beta) + complex(0,1)*kap*TH4x3*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta) - 2*alp1*complex(0,1)*kk*TH1x3*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*kk*TH1x3*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x3*vL*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x3*vR*cmath.sin(beta)**2',
                  order = {'QED':1})

GC_761 = Coupling(name = 'GC_761',
                  value = '-2*complex(0,1)*kk*lam1*TH1x4*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH3x4*vL*cmath.cos(beta)**2 - 2*alp3*complex(0,1)*TH3x4*vL*cmath.cos(beta)**2 - 2*alp1*complex(0,1)*TH4x4*vR*cmath.cos(beta)**2 - 2*alp2*complex(0,1)*TH4x4*vR*cmath.cos(beta)**2 + 2*alp2*complex(0,1)*kk*TH3x4*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*kk*TH3x4*cmath.cos(beta)*cmath.sin(beta) + 2*alp2*complex(0,1)*TH1x4*vL*cmath.cos(beta)*cmath.sin(beta) - 2*alp3*complex(0,1)*TH1x4*vL*cmath.cos(beta)*cmath.sin(beta) + complex(0,1)*kap*TH4x4*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta) - 2*alp1*complex(0,1)*kk*TH1x4*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*kk*TH1x4*cmath.sin(beta)**2 - 2*complex(0,1)*lam3*TH3x4*vL*cmath.sin(beta)**2 - 2*complex(0,1)*lam4*TH4x4*vR*cmath.sin(beta)**2',
                  order = {'QED':1})

GC_762 = Coupling(name = 'GC_762',
                  value = '-4*complex(0,1)*lam1*cmath.cos(beta)**4 - 8*alp1*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2 - 8*alp2*complex(0,1)*cmath.cos(beta)**2*cmath.sin(beta)**2 - 4*complex(0,1)*lam3*cmath.sin(beta)**4',
                  order = {'QED':2})

GC_763 = Coupling(name = 'GC_763',
                  value = 'complex(0,1)*I15b11*cmath.sin(zeta)',
                  order = {'QED':1})

GC_764 = Coupling(name = 'GC_764',
                  value = 'complex(0,1)*I15b12*cmath.sin(zeta)',
                  order = {'QED':1})

GC_765 = Coupling(name = 'GC_765',
                  value = 'complex(0,1)*I15b13*cmath.sin(zeta)',
                  order = {'QED':1})

GC_766 = Coupling(name = 'GC_766',
                  value = 'complex(0,1)*I15b21*cmath.sin(zeta)',
                  order = {'QED':1})

GC_767 = Coupling(name = 'GC_767',
                  value = 'complex(0,1)*I15b22*cmath.sin(zeta)',
                  order = {'QED':1})

GC_768 = Coupling(name = 'GC_768',
                  value = 'complex(0,1)*I15b23*cmath.sin(zeta)',
                  order = {'QED':1})

GC_769 = Coupling(name = 'GC_769',
                  value = 'complex(0,1)*I15b31*cmath.sin(zeta)',
                  order = {'QED':1})

GC_770 = Coupling(name = 'GC_770',
                  value = 'complex(0,1)*I15b32*cmath.sin(zeta)',
                  order = {'QED':1})

GC_771 = Coupling(name = 'GC_771',
                  value = 'complex(0,1)*I15b33*cmath.sin(zeta)',
                  order = {'QED':1})

GC_772 = Coupling(name = 'GC_772',
                  value = '-(complex(0,1)*I19b11*cmath.sin(zeta))',
                  order = {'QED':1})

GC_773 = Coupling(name = 'GC_773',
                  value = '-(complex(0,1)*I19b12*cmath.sin(zeta))',
                  order = {'QED':1})

GC_774 = Coupling(name = 'GC_774',
                  value = '-(complex(0,1)*I19b13*cmath.sin(zeta))',
                  order = {'QED':1})

GC_775 = Coupling(name = 'GC_775',
                  value = '-(complex(0,1)*I19b21*cmath.sin(zeta))',
                  order = {'QED':1})

GC_776 = Coupling(name = 'GC_776',
                  value = '-(complex(0,1)*I19b22*cmath.sin(zeta))',
                  order = {'QED':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(complex(0,1)*I19b23*cmath.sin(zeta))',
                  order = {'QED':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '-(complex(0,1)*I19b31*cmath.sin(zeta))',
                  order = {'QED':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '-(complex(0,1)*I19b32*cmath.sin(zeta))',
                  order = {'QED':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '-(complex(0,1)*I19b33*cmath.sin(zeta))',
                  order = {'QED':1})

GC_781 = Coupling(name = 'GC_781',
                  value = 'complex(0,1)*I3b11*cmath.sin(zeta)',
                  order = {'QED':1})

GC_782 = Coupling(name = 'GC_782',
                  value = 'complex(0,1)*I3b12*cmath.sin(zeta)',
                  order = {'QED':1})

GC_783 = Coupling(name = 'GC_783',
                  value = 'complex(0,1)*I3b13*cmath.sin(zeta)',
                  order = {'QED':1})

GC_784 = Coupling(name = 'GC_784',
                  value = 'complex(0,1)*I3b21*cmath.sin(zeta)',
                  order = {'QED':1})

GC_785 = Coupling(name = 'GC_785',
                  value = 'complex(0,1)*I3b22*cmath.sin(zeta)',
                  order = {'QED':1})

GC_786 = Coupling(name = 'GC_786',
                  value = 'complex(0,1)*I3b23*cmath.sin(zeta)',
                  order = {'QED':1})

GC_787 = Coupling(name = 'GC_787',
                  value = 'complex(0,1)*I3b31*cmath.sin(zeta)',
                  order = {'QED':1})

GC_788 = Coupling(name = 'GC_788',
                  value = 'complex(0,1)*I3b32*cmath.sin(zeta)',
                  order = {'QED':1})

GC_789 = Coupling(name = 'GC_789',
                  value = 'complex(0,1)*I3b33*cmath.sin(zeta)',
                  order = {'QED':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '-(complex(0,1)*I9b11*cmath.sin(zeta))',
                  order = {'QED':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '-(complex(0,1)*I9b12*cmath.sin(zeta))',
                  order = {'QED':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '-(complex(0,1)*I9b13*cmath.sin(zeta))',
                  order = {'QED':1})

GC_793 = Coupling(name = 'GC_793',
                  value = '-(complex(0,1)*I9b21*cmath.sin(zeta))',
                  order = {'QED':1})

GC_794 = Coupling(name = 'GC_794',
                  value = '-(complex(0,1)*I9b22*cmath.sin(zeta))',
                  order = {'QED':1})

GC_795 = Coupling(name = 'GC_795',
                  value = '-(complex(0,1)*I9b23*cmath.sin(zeta))',
                  order = {'QED':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '-(complex(0,1)*I9b31*cmath.sin(zeta))',
                  order = {'QED':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '-(complex(0,1)*I9b32*cmath.sin(zeta))',
                  order = {'QED':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '-(complex(0,1)*I9b33*cmath.sin(zeta))',
                  order = {'QED':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '(complex(0,1)*gR*TH1x1*cmath.cos(zeta))/2. - (complex(0,1)*gR*TH4x1*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_800 = Coupling(name = 'GC_800',
                  value = '-(complex(0,1)*gR*TH1x1*cmath.cos(zeta))/2. + (complex(0,1)*gR*TH4x1*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_801 = Coupling(name = 'GC_801',
                  value = '(complex(0,1)*gL*gR*sw*TH1x1*cmath.cos(zeta))/2. - (cph*cw*complex(0,1)*gBL*gR*TH4x1*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_802 = Coupling(name = 'GC_802',
                  value = '(ct*cw*complex(0,1)*gL*gR*TH1x1*cmath.cos(zeta))/2. + (complex(0,1)*gBL*gR*sph*st*TH4x1*cmath.sin(zeta))/2. + (cph*ct*complex(0,1)*gBL*gR*sw*TH4x1*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_803 = Coupling(name = 'GC_803',
                  value = '-(cw*complex(0,1)*gL*gR*st*TH1x1*cmath.cos(zeta))/2. + (ct*complex(0,1)*gBL*gR*sph*TH4x1*cmath.sin(zeta))/2. - (cph*complex(0,1)*gBL*gR*st*sw*TH4x1*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_804 = Coupling(name = 'GC_804',
                  value = '(complex(0,1)*gR*TH1x2*cmath.cos(zeta))/2. - (complex(0,1)*gR*TH4x2*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_805 = Coupling(name = 'GC_805',
                  value = '-(complex(0,1)*gR*TH1x2*cmath.cos(zeta))/2. + (complex(0,1)*gR*TH4x2*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_806 = Coupling(name = 'GC_806',
                  value = '(complex(0,1)*gL*gR*sw*TH1x2*cmath.cos(zeta))/2. - (cph*cw*complex(0,1)*gBL*gR*TH4x2*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_807 = Coupling(name = 'GC_807',
                  value = '(ct*cw*complex(0,1)*gL*gR*TH1x2*cmath.cos(zeta))/2. + (complex(0,1)*gBL*gR*sph*st*TH4x2*cmath.sin(zeta))/2. + (cph*ct*complex(0,1)*gBL*gR*sw*TH4x2*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_808 = Coupling(name = 'GC_808',
                  value = '-(cw*complex(0,1)*gL*gR*st*TH1x2*cmath.cos(zeta))/2. + (ct*complex(0,1)*gBL*gR*sph*TH4x2*cmath.sin(zeta))/2. - (cph*complex(0,1)*gBL*gR*st*sw*TH4x2*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_809 = Coupling(name = 'GC_809',
                  value = '(complex(0,1)*gR*TH1x3*cmath.cos(zeta))/2. - (complex(0,1)*gR*TH4x3*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_810 = Coupling(name = 'GC_810',
                  value = '-(complex(0,1)*gR*TH1x3*cmath.cos(zeta))/2. + (complex(0,1)*gR*TH4x3*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '(complex(0,1)*gL*gR*sw*TH1x3*cmath.cos(zeta))/2. - (cph*cw*complex(0,1)*gBL*gR*TH4x3*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_812 = Coupling(name = 'GC_812',
                  value = '(ct*cw*complex(0,1)*gL*gR*TH1x3*cmath.cos(zeta))/2. + (complex(0,1)*gBL*gR*sph*st*TH4x3*cmath.sin(zeta))/2. + (cph*ct*complex(0,1)*gBL*gR*sw*TH4x3*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_813 = Coupling(name = 'GC_813',
                  value = '-(cw*complex(0,1)*gL*gR*st*TH1x3*cmath.cos(zeta))/2. + (ct*complex(0,1)*gBL*gR*sph*TH4x3*cmath.sin(zeta))/2. - (cph*complex(0,1)*gBL*gR*st*sw*TH4x3*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_814 = Coupling(name = 'GC_814',
                  value = '(complex(0,1)*gR*TH1x4*cmath.cos(zeta))/2. - (complex(0,1)*gR*TH4x4*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '-(complex(0,1)*gR*TH1x4*cmath.cos(zeta))/2. + (complex(0,1)*gR*TH4x4*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '(complex(0,1)*gL*gR*sw*TH1x4*cmath.cos(zeta))/2. - (cph*cw*complex(0,1)*gBL*gR*TH4x4*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_817 = Coupling(name = 'GC_817',
                  value = '(ct*cw*complex(0,1)*gL*gR*TH1x4*cmath.cos(zeta))/2. + (complex(0,1)*gBL*gR*sph*st*TH4x4*cmath.sin(zeta))/2. + (cph*ct*complex(0,1)*gBL*gR*sw*TH4x4*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_818 = Coupling(name = 'GC_818',
                  value = '-(cw*complex(0,1)*gL*gR*st*TH1x4*cmath.cos(zeta))/2. + (ct*complex(0,1)*gBL*gR*sph*TH4x4*cmath.sin(zeta))/2. - (cph*complex(0,1)*gBL*gR*st*sw*TH4x4*cmath.sin(zeta))/2.',
                  order = {'QED':2})

GC_819 = Coupling(name = 'GC_819',
                  value = '-(gR*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gR*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':1})

GC_820 = Coupling(name = 'GC_820',
                  value = '-(gL*gR*sw*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*cw*gBL*gR*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_821 = Coupling(name = 'GC_821',
                  value = '(gL*gR*sw*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*cw*gBL*gR*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_822 = Coupling(name = 'GC_822',
                  value = '(ct*cw*gL*gR*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (gBL*gR*sph*st*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*ct*gBL*gR*sw*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_823 = Coupling(name = 'GC_823',
                  value = '-(ct*cw*gL*gR*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (gBL*gR*sph*st*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*ct*gBL*gR*sw*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_824 = Coupling(name = 'GC_824',
                  value = '(cw*gL*gR*st*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (ct*gBL*gR*sph*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (cph*gBL*gR*st*sw*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '-(cw*gL*gR*st*cmath.cos(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) - (ct*gBL*gR*sph*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2)) + (cph*gBL*gR*st*sw*tz*cmath.sin(zeta))/(2.*cmath.sqrt(1 + tb**2 + tz**2))',
                  order = {'QED':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '(complex(0,1)*gL*gR*kk*sw*cmath.cos(zeta))/2. - (cph*cw*complex(0,1)*gBL*gR*vR*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_827 = Coupling(name = 'GC_827',
                  value = '(ct*cw*complex(0,1)*gL*gR*kk*cmath.cos(zeta))/2. + (complex(0,1)*gBL*gR*sph*st*vR*cmath.sin(zeta))/2. + (cph*ct*complex(0,1)*gBL*gR*sw*vR*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_828 = Coupling(name = 'GC_828',
                  value = '-(cw*complex(0,1)*gL*gR*kk*st*cmath.cos(zeta))/2. + (ct*complex(0,1)*gBL*gR*sph*vR*cmath.sin(zeta))/2. - (cph*complex(0,1)*gBL*gR*st*sw*vR*cmath.sin(zeta))/2.',
                  order = {'QED':1})

GC_829 = Coupling(name = 'GC_829',
                  value = '2*lam2*TH1x1*cmath.cos(beta)*cmath.cos(zeta) + alp2*TH3x1*cmath.cos(zeta)*cmath.sin(beta) - alp3*TH3x1*cmath.cos(zeta)*cmath.sin(beta) + alp2*TH4x1*cmath.cos(beta)*cmath.sin(zeta) - alp3*TH4x1*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '2*complex(0,1)*lam2*TH1x1*cmath.cos(beta)*cmath.cos(zeta) + alp2*complex(0,1)*TH3x1*cmath.cos(zeta)*cmath.sin(beta) - alp3*complex(0,1)*TH3x1*cmath.cos(zeta)*cmath.sin(beta) + alp2*complex(0,1)*TH4x1*cmath.cos(beta)*cmath.sin(zeta) - alp3*complex(0,1)*TH4x1*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '-2*lam2*TH1x1*cmath.cos(beta)*cmath.cos(zeta) - alp2*TH3x1*cmath.cos(zeta)*cmath.sin(beta) + alp3*TH3x1*cmath.cos(zeta)*cmath.sin(beta) - alp2*TH4x1*cmath.cos(beta)*cmath.sin(zeta) + alp3*TH4x1*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '2*lam2*TH1x2*cmath.cos(beta)*cmath.cos(zeta) + alp2*TH3x2*cmath.cos(zeta)*cmath.sin(beta) - alp3*TH3x2*cmath.cos(zeta)*cmath.sin(beta) + alp2*TH4x2*cmath.cos(beta)*cmath.sin(zeta) - alp3*TH4x2*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '2*complex(0,1)*lam2*TH1x2*cmath.cos(beta)*cmath.cos(zeta) + alp2*complex(0,1)*TH3x2*cmath.cos(zeta)*cmath.sin(beta) - alp3*complex(0,1)*TH3x2*cmath.cos(zeta)*cmath.sin(beta) + alp2*complex(0,1)*TH4x2*cmath.cos(beta)*cmath.sin(zeta) - alp3*complex(0,1)*TH4x2*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_834 = Coupling(name = 'GC_834',
                  value = '-2*lam2*TH1x2*cmath.cos(beta)*cmath.cos(zeta) - alp2*TH3x2*cmath.cos(zeta)*cmath.sin(beta) + alp3*TH3x2*cmath.cos(zeta)*cmath.sin(beta) - alp2*TH4x2*cmath.cos(beta)*cmath.sin(zeta) + alp3*TH4x2*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_835 = Coupling(name = 'GC_835',
                  value = '2*lam2*TH1x3*cmath.cos(beta)*cmath.cos(zeta) + alp2*TH3x3*cmath.cos(zeta)*cmath.sin(beta) - alp3*TH3x3*cmath.cos(zeta)*cmath.sin(beta) + alp2*TH4x3*cmath.cos(beta)*cmath.sin(zeta) - alp3*TH4x3*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_836 = Coupling(name = 'GC_836',
                  value = '2*complex(0,1)*lam2*TH1x3*cmath.cos(beta)*cmath.cos(zeta) + alp2*complex(0,1)*TH3x3*cmath.cos(zeta)*cmath.sin(beta) - alp3*complex(0,1)*TH3x3*cmath.cos(zeta)*cmath.sin(beta) + alp2*complex(0,1)*TH4x3*cmath.cos(beta)*cmath.sin(zeta) - alp3*complex(0,1)*TH4x3*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_837 = Coupling(name = 'GC_837',
                  value = '-2*lam2*TH1x3*cmath.cos(beta)*cmath.cos(zeta) - alp2*TH3x3*cmath.cos(zeta)*cmath.sin(beta) + alp3*TH3x3*cmath.cos(zeta)*cmath.sin(beta) - alp2*TH4x3*cmath.cos(beta)*cmath.sin(zeta) + alp3*TH4x3*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_838 = Coupling(name = 'GC_838',
                  value = '2*lam2*TH1x4*cmath.cos(beta)*cmath.cos(zeta) + alp2*TH3x4*cmath.cos(zeta)*cmath.sin(beta) - alp3*TH3x4*cmath.cos(zeta)*cmath.sin(beta) + alp2*TH4x4*cmath.cos(beta)*cmath.sin(zeta) - alp3*TH4x4*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_839 = Coupling(name = 'GC_839',
                  value = '2*complex(0,1)*lam2*TH1x4*cmath.cos(beta)*cmath.cos(zeta) + alp2*complex(0,1)*TH3x4*cmath.cos(zeta)*cmath.sin(beta) - alp3*complex(0,1)*TH3x4*cmath.cos(zeta)*cmath.sin(beta) + alp2*complex(0,1)*TH4x4*cmath.cos(beta)*cmath.sin(zeta) - alp3*complex(0,1)*TH4x4*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_840 = Coupling(name = 'GC_840',
                  value = '-2*lam2*TH1x4*cmath.cos(beta)*cmath.cos(zeta) - alp2*TH3x4*cmath.cos(zeta)*cmath.sin(beta) + alp3*TH3x4*cmath.cos(zeta)*cmath.sin(beta) - alp2*TH4x4*cmath.cos(beta)*cmath.sin(zeta) + alp3*TH4x4*cmath.cos(beta)*cmath.sin(zeta)',
                  order = {'QED':2})

GC_841 = Coupling(name = 'GC_841',
                  value = '(-2*lam2*cmath.cos(beta)*cmath.cos(zeta))/cmath.sqrt(1 + tb**2 + tz**2) + (alp2*tb*cmath.cos(zeta)*cmath.sin(beta))/cmath.sqrt(1 + tb**2 + tz**2) - (alp3*tb*cmath.cos(zeta)*cmath.sin(beta))/cmath.sqrt(1 + tb**2 + tz**2) + (alp2*tz*cmath.cos(beta)*cmath.sin(zeta))/cmath.sqrt(1 + tb**2 + tz**2) - (alp3*tz*cmath.cos(beta)*cmath.sin(zeta))/cmath.sqrt(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_842 = Coupling(name = 'GC_842',
                  value = '(-2*complex(0,1)*lam2*cmath.cos(beta)*cmath.cos(zeta))/cmath.sqrt(1 + tb**2 + tz**2) + (alp2*complex(0,1)*tb*cmath.cos(zeta)*cmath.sin(beta))/cmath.sqrt(1 + tb**2 + tz**2) - (alp3*complex(0,1)*tb*cmath.cos(zeta)*cmath.sin(beta))/cmath.sqrt(1 + tb**2 + tz**2) + (alp2*complex(0,1)*tz*cmath.cos(beta)*cmath.sin(zeta))/cmath.sqrt(1 + tb**2 + tz**2) - (alp3*complex(0,1)*tz*cmath.cos(beta)*cmath.sin(zeta))/cmath.sqrt(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_843 = Coupling(name = 'GC_843',
                  value = '(2*lam2*cmath.cos(beta)*cmath.cos(zeta))/cmath.sqrt(1 + tb**2 + tz**2) - (alp2*tb*cmath.cos(zeta)*cmath.sin(beta))/cmath.sqrt(1 + tb**2 + tz**2) + (alp3*tb*cmath.cos(zeta)*cmath.sin(beta))/cmath.sqrt(1 + tb**2 + tz**2) - (alp2*tz*cmath.cos(beta)*cmath.sin(zeta))/cmath.sqrt(1 + tb**2 + tz**2) + (alp3*tz*cmath.cos(beta)*cmath.sin(zeta))/cmath.sqrt(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_844 = Coupling(name = 'GC_844',
                  value = '2*kk*lam2*cmath.cos(beta)*cmath.cos(zeta) + alp2*vL*cmath.cos(zeta)*cmath.sin(beta) - alp3*vL*cmath.cos(zeta)*cmath.sin(beta) + alp2*vR*cmath.cos(beta)*cmath.sin(zeta) - alp3*vR*cmath.cos(beta)*cmath.sin(zeta) - (kap*cmath.sin(beta)*cmath.sin(zeta))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_845 = Coupling(name = 'GC_845',
                  value = '2*complex(0,1)*kk*lam2*cmath.cos(beta)*cmath.cos(zeta) + alp2*complex(0,1)*vL*cmath.cos(zeta)*cmath.sin(beta) - alp3*complex(0,1)*vL*cmath.cos(zeta)*cmath.sin(beta) + alp2*complex(0,1)*vR*cmath.cos(beta)*cmath.sin(zeta) - alp3*complex(0,1)*vR*cmath.cos(beta)*cmath.sin(zeta) - (complex(0,1)*kap*cmath.sin(beta)*cmath.sin(zeta))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_846 = Coupling(name = 'GC_846',
                  value = '-2*kk*lam2*cmath.cos(beta)*cmath.cos(zeta) - alp2*vL*cmath.cos(zeta)*cmath.sin(beta) + alp3*vL*cmath.cos(zeta)*cmath.sin(beta) - alp2*vR*cmath.cos(beta)*cmath.sin(zeta) + alp3*vR*cmath.cos(beta)*cmath.sin(zeta) + (kap*cmath.sin(beta)*cmath.sin(zeta))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_847 = Coupling(name = 'GC_847',
                  value = '-2*complex(0,1)*lam1*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*cmath.sin(zeta)**2 - 2*alp2*complex(0,1)*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_848 = Coupling(name = 'GC_848',
                  value = '(complex(0,1)*gR**2*cmath.cos(zeta)**2)/2. + (complex(0,1)*gR**2*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_849 = Coupling(name = 'GC_849',
                  value = '-(cw*complex(0,1)*gR*sph*cmath.cos(zeta)**2)/2. - (complex(0,1)*gL*sw*cmath.cos(zeta)**2)/2. - (cph*cw*complex(0,1)*gBL*cmath.sin(zeta)**2)/2. - (cw*complex(0,1)*gR*sph*cmath.sin(zeta)**2)/2.',
                  order = {'QED':1})

GC_850 = Coupling(name = 'GC_850',
                  value = '(cw*complex(0,1)*gR*sph*cmath.cos(zeta)**2)/2. + (complex(0,1)*gL*sw*cmath.cos(zeta)**2)/2. + (cph*cw*complex(0,1)*gBL*cmath.sin(zeta)**2)/2. + (cw*complex(0,1)*gR*sph*cmath.sin(zeta)**2)/2.',
                  order = {'QED':1})

GC_851 = Coupling(name = 'GC_851',
                  value = '(cw**2*complex(0,1)*gR**2*sph**2*cmath.cos(zeta)**2)/2. + cw*complex(0,1)*gL*gR*sph*sw*cmath.cos(zeta)**2 + (complex(0,1)*gL**2*sw**2*cmath.cos(zeta)**2)/2. + (cph**2*cw**2*complex(0,1)*gBL**2*cmath.sin(zeta)**2)/2. + cph*cw**2*complex(0,1)*gBL*gR*sph*cmath.sin(zeta)**2 + (cw**2*complex(0,1)*gR**2*sph**2*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_852 = Coupling(name = 'GC_852',
                  value = '-(ct*cw*complex(0,1)*gL*cmath.cos(zeta)**2)/2. - (cph*complex(0,1)*gR*st*cmath.cos(zeta)**2)/2. + (ct*complex(0,1)*gR*sph*sw*cmath.cos(zeta)**2)/2. - (cph*complex(0,1)*gR*st*cmath.sin(zeta)**2)/2. + (complex(0,1)*gBL*sph*st*cmath.sin(zeta)**2)/2. + (cph*ct*complex(0,1)*gBL*sw*cmath.sin(zeta)**2)/2. + (ct*complex(0,1)*gR*sph*sw*cmath.sin(zeta)**2)/2.',
                  order = {'QED':1})

GC_853 = Coupling(name = 'GC_853',
                  value = '(ct*cw**2*complex(0,1)*gL*gR*sph*cmath.cos(zeta)**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*cmath.cos(zeta)**2)/2. + (ct*cw*complex(0,1)*gL**2*sw*cmath.cos(zeta)**2)/2. - (ct*cw*complex(0,1)*gR**2*sph**2*sw*cmath.cos(zeta)**2)/2. + (cph*complex(0,1)*gL*gR*st*sw*cmath.cos(zeta)**2)/2. - (ct*complex(0,1)*gL*gR*sph*sw**2*cmath.cos(zeta)**2)/2. + (cph**2*cw*complex(0,1)*gBL*gR*st*cmath.sin(zeta)**2)/2. - (cph*cw*complex(0,1)*gBL**2*sph*st*cmath.sin(zeta)**2)/2. + (cph*cw*complex(0,1)*gR**2*sph*st*cmath.sin(zeta)**2)/2. - (cw*complex(0,1)*gBL*gR*sph**2*st*cmath.sin(zeta)**2)/2. - (cph**2*ct*cw*complex(0,1)*gBL**2*sw*cmath.sin(zeta)**2)/2. - cph*ct*cw*complex(0,1)*gBL*gR*sph*sw*cmath.sin(zeta)**2 - (ct*cw*complex(0,1)*gR**2*sph**2*sw*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_854 = Coupling(name = 'GC_854',
                  value = '-(cph*ct*complex(0,1)*gR*cmath.cos(zeta)**2)/2. + (cw*complex(0,1)*gL*st*cmath.cos(zeta)**2)/2. - (complex(0,1)*gR*sph*st*sw*cmath.cos(zeta)**2)/2. - (cph*ct*complex(0,1)*gR*cmath.sin(zeta)**2)/2. + (ct*complex(0,1)*gBL*sph*cmath.sin(zeta)**2)/2. - (cph*complex(0,1)*gBL*st*sw*cmath.sin(zeta)**2)/2. - (complex(0,1)*gR*sph*st*sw*cmath.sin(zeta)**2)/2.',
                  order = {'QED':1})

GC_855 = Coupling(name = 'GC_855',
                  value = '(cph*ct*cw*complex(0,1)*gR**2*sph*cmath.cos(zeta)**2)/2. - (cw**2*complex(0,1)*gL*gR*sph*st*cmath.cos(zeta)**2)/2. + (cph*ct*complex(0,1)*gL*gR*sw*cmath.cos(zeta)**2)/2. - (cw*complex(0,1)*gL**2*st*sw*cmath.cos(zeta)**2)/2. + (cw*complex(0,1)*gR**2*sph**2*st*sw*cmath.cos(zeta)**2)/2. + (complex(0,1)*gL*gR*sph*st*sw**2*cmath.cos(zeta)**2)/2. + (cph**2*ct*cw*complex(0,1)*gBL*gR*cmath.sin(zeta)**2)/2. - (cph*ct*cw*complex(0,1)*gBL**2*sph*cmath.sin(zeta)**2)/2. + (cph*ct*cw*complex(0,1)*gR**2*sph*cmath.sin(zeta)**2)/2. - (ct*cw*complex(0,1)*gBL*gR*sph**2*cmath.sin(zeta)**2)/2. + (cph**2*cw*complex(0,1)*gBL**2*st*sw*cmath.sin(zeta)**2)/2. + cph*cw*complex(0,1)*gBL*gR*sph*st*sw*cmath.sin(zeta)**2 + (cw*complex(0,1)*gR**2*sph**2*st*sw*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_856 = Coupling(name = 'GC_856',
                  value = '(ct**2*cw**2*complex(0,1)*gL**2*cmath.cos(zeta)**2)/2. + cph*ct*cw*complex(0,1)*gL*gR*st*cmath.cos(zeta)**2 + (cph**2*complex(0,1)*gR**2*st**2*cmath.cos(zeta)**2)/2. - ct**2*cw*complex(0,1)*gL*gR*sph*sw*cmath.cos(zeta)**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*cmath.cos(zeta)**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*cmath.cos(zeta)**2)/2. + (cph**2*complex(0,1)*gR**2*st**2*cmath.sin(zeta)**2)/2. - cph*complex(0,1)*gBL*gR*sph*st**2*cmath.sin(zeta)**2 + (complex(0,1)*gBL**2*sph**2*st**2*cmath.sin(zeta)**2)/2. - cph**2*ct*complex(0,1)*gBL*gR*st*sw*cmath.sin(zeta)**2 + cph*ct*complex(0,1)*gBL**2*sph*st*sw*cmath.sin(zeta)**2 - cph*ct*complex(0,1)*gR**2*sph*st*sw*cmath.sin(zeta)**2 + ct*complex(0,1)*gBL*gR*sph**2*st*sw*cmath.sin(zeta)**2 + (cph**2*ct**2*complex(0,1)*gBL**2*sw**2*cmath.sin(zeta)**2)/2. + cph*ct**2*complex(0,1)*gBL*gR*sph*sw**2*cmath.sin(zeta)**2 + (ct**2*complex(0,1)*gR**2*sph**2*sw**2*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '(cph*ct**2*cw*complex(0,1)*gL*gR*cmath.cos(zeta)**2)/2. - (ct*cw**2*complex(0,1)*gL**2*st*cmath.cos(zeta)**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*cmath.cos(zeta)**2)/2. - (cph*cw*complex(0,1)*gL*gR*st**2*cmath.cos(zeta)**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*cmath.cos(zeta)**2)/2. + ct*cw*complex(0,1)*gL*gR*sph*st*sw*cmath.cos(zeta)**2 + (cph*complex(0,1)*gR**2*sph*st**2*sw*cmath.cos(zeta)**2)/2. - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*cmath.cos(zeta)**2)/2. + (cph**2*ct*complex(0,1)*gR**2*st*cmath.sin(zeta)**2)/2. - cph*ct*complex(0,1)*gBL*gR*sph*st*cmath.sin(zeta)**2 + (ct*complex(0,1)*gBL**2*sph**2*st*cmath.sin(zeta)**2)/2. - (cph**2*ct**2*complex(0,1)*gBL*gR*sw*cmath.sin(zeta)**2)/2. + (cph*ct**2*complex(0,1)*gBL**2*sph*sw*cmath.sin(zeta)**2)/2. - (cph*ct**2*complex(0,1)*gR**2*sph*sw*cmath.sin(zeta)**2)/2. + (ct**2*complex(0,1)*gBL*gR*sph**2*sw*cmath.sin(zeta)**2)/2. + (cph**2*complex(0,1)*gBL*gR*st**2*sw*cmath.sin(zeta)**2)/2. - (cph*complex(0,1)*gBL**2*sph*st**2*sw*cmath.sin(zeta)**2)/2. + (cph*complex(0,1)*gR**2*sph*st**2*sw*cmath.sin(zeta)**2)/2. - (complex(0,1)*gBL*gR*sph**2*st**2*sw*cmath.sin(zeta)**2)/2. - (cph**2*ct*complex(0,1)*gBL**2*st*sw**2*cmath.sin(zeta)**2)/2. - cph*ct*complex(0,1)*gBL*gR*sph*st*sw**2*cmath.sin(zeta)**2 - (ct*complex(0,1)*gR**2*sph**2*st*sw**2*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '(cph**2*ct**2*complex(0,1)*gR**2*cmath.cos(zeta)**2)/2. - cph*ct*cw*complex(0,1)*gL*gR*st*cmath.cos(zeta)**2 + (cw**2*complex(0,1)*gL**2*st**2*cmath.cos(zeta)**2)/2. + cph*ct*complex(0,1)*gR**2*sph*st*sw*cmath.cos(zeta)**2 - cw*complex(0,1)*gL*gR*sph*st**2*sw*cmath.cos(zeta)**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*cmath.cos(zeta)**2)/2. + (cph**2*ct**2*complex(0,1)*gR**2*cmath.sin(zeta)**2)/2. - cph*ct**2*complex(0,1)*gBL*gR*sph*cmath.sin(zeta)**2 + (ct**2*complex(0,1)*gBL**2*sph**2*cmath.sin(zeta)**2)/2. + cph**2*ct*complex(0,1)*gBL*gR*st*sw*cmath.sin(zeta)**2 - cph*ct*complex(0,1)*gBL**2*sph*st*sw*cmath.sin(zeta)**2 + cph*ct*complex(0,1)*gR**2*sph*st*sw*cmath.sin(zeta)**2 - ct*complex(0,1)*gBL*gR*sph**2*st*sw*cmath.sin(zeta)**2 + (cph**2*complex(0,1)*gBL**2*st**2*sw**2*cmath.sin(zeta)**2)/2. + cph*complex(0,1)*gBL*gR*sph*st**2*sw**2*cmath.sin(zeta)**2 + (complex(0,1)*gR**2*sph**2*st**2*sw**2*cmath.sin(zeta)**2)/2.',
                  order = {'QED':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '-2*complex(0,1)*lam1*TH1x1**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x1**2*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x1**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x1**2*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x1**2*cmath.cos(zeta)**2 + 4*alp2*complex(0,1)*TH1x1*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) - 4*alp3*complex(0,1)*TH1x1*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x1**2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x1**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x1**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x1**2*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x1*TH3x2*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x1*TH3x2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x1*TH4x2*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x1*TH4x2*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*TH1x2*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x2*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x1*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x1*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x1*TH1x2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x1*TH1x2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x1*TH3x2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x1*TH4x2*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_861 = Coupling(name = 'GC_861',
                  value = '-2*complex(0,1)*lam1*cmath.cos(zeta)**2 - 2*complex(0,1)*lam1*TH1x2**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x2**2*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x2**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x2**2*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x2**2*cmath.cos(zeta)**2 + 4*alp2*complex(0,1)*TH1x2*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 4*alp3*complex(0,1)*TH1x2*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*cmath.sin(zeta)**2 - 2*alp2*complex(0,1)*cmath.sin(zeta)**2 - 2*alp1*complex(0,1)*TH1x2**2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x2**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x2**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x2**2*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_862 = Coupling(name = 'GC_862',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x3*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x1*TH3x3*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x1*TH3x3*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x1*TH4x3*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x1*TH4x3*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*TH1x3*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x3*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x1*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x1*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x1*TH1x3*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x1*TH1x3*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x1*TH3x3*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x1*TH4x3*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_863 = Coupling(name = 'GC_863',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x3*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x2*TH3x3*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x2*TH3x3*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x2*TH4x3*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x2*TH4x3*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*TH1x3*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x3*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x2*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x2*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x2*TH1x3*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x2*TH1x3*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x2*TH3x3*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x2*TH4x3*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_864 = Coupling(name = 'GC_864',
                  value = '-2*complex(0,1)*lam1*TH1x3**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x3**2*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x3**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x3**2*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x3**2*cmath.cos(zeta)**2 + 4*alp2*complex(0,1)*TH1x3*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 4*alp3*complex(0,1)*TH1x3*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x3**2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x3**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x3**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x3**2*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_865 = Coupling(name = 'GC_865',
                  value = '-2*complex(0,1)*lam1*TH1x1*TH1x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x1*TH3x4*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x1*TH3x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x1*TH4x4*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x1*TH4x4*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*TH1x4*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x4*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x1*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x1*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x1*TH1x4*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x1*TH1x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x1*TH3x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x1*TH4x4*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_866 = Coupling(name = 'GC_866',
                  value = '-2*complex(0,1)*lam1*TH1x2*TH1x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x2*TH3x4*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x2*TH3x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x2*TH4x4*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x2*TH4x4*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*TH1x4*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x4*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x2*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x2*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x2*TH1x4*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x2*TH1x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x2*TH3x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x2*TH4x4*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_867 = Coupling(name = 'GC_867',
                  value = '-2*complex(0,1)*lam1*TH1x3*TH1x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x3*TH3x4*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x3*TH3x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x3*TH4x4*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x3*TH4x4*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*TH1x4*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x4*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x3*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x3*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x3*TH1x4*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x3*TH1x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x3*TH3x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x3*TH4x4*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_868 = Coupling(name = 'GC_868',
                  value = '-2*complex(0,1)*lam1*TH1x4**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x4**2*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x4**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x4**2*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x4**2*cmath.cos(zeta)**2 + 4*alp2*complex(0,1)*TH1x4*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 4*alp3*complex(0,1)*TH1x4*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp1*complex(0,1)*TH1x4**2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*TH1x4**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x4**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x4**2*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_869 = Coupling(name = 'GC_869',
                  value = '(-2*complex(0,1)*lam1*cmath.cos(zeta)**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tb**2*cmath.cos(zeta)**2)/(1 + tb**2 + tz**2) - (2*alp2*complex(0,1)*tb**2*cmath.cos(zeta)**2)/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*tz**2*cmath.cos(zeta)**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*tz**2*cmath.cos(zeta)**2)/(1 + tb**2 + tz**2) - (4*alp2*complex(0,1)*tz*cmath.cos(zeta)*cmath.sin(zeta))/(1 + tb**2 + tz**2) + (4*alp3*complex(0,1)*tz*cmath.cos(zeta)*cmath.sin(zeta))/(1 + tb**2 + tz**2) - (2*alp1*complex(0,1)*cmath.sin(zeta)**2)/(1 + tb**2 + tz**2) - (2*alp3*complex(0,1)*cmath.sin(zeta)**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam4*tb**2*cmath.sin(zeta)**2)/(1 + tb**2 + tz**2) - (2*complex(0,1)*lam3*tz**2*cmath.sin(zeta)**2)/(1 + tb**2 + tz**2)',
                  order = {'QED':2})

GC_870 = Coupling(name = 'GC_870',
                  value = '-2*complex(0,1)*kk*lam1*TH1x1*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x1*vL*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x1*vL*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x1*vR*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x1*vR*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*kk*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*kk*TH4x1*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x1*vR*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x1*vR*cmath.cos(zeta)*cmath.sin(zeta) + complex(0,1)*kap*TH3x1*cmath.cos(zeta)*cmath.sqrt(2)*cmath.sin(zeta) - 2*alp1*complex(0,1)*kk*TH1x1*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*kk*TH1x1*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x1*vL*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x1*vR*cmath.sin(zeta)**2',
                  order = {'QED':1})

GC_871 = Coupling(name = 'GC_871',
                  value = '-2*complex(0,1)*kk*lam1*TH1x2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x2*vL*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x2*vL*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x2*vR*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x2*vR*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*kk*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*kk*TH4x2*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x2*vR*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x2*vR*cmath.cos(zeta)*cmath.sin(zeta) + complex(0,1)*kap*TH3x2*cmath.cos(zeta)*cmath.sqrt(2)*cmath.sin(zeta) - 2*alp1*complex(0,1)*kk*TH1x2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*kk*TH1x2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x2*vL*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x2*vR*cmath.sin(zeta)**2',
                  order = {'QED':1})

GC_872 = Coupling(name = 'GC_872',
                  value = '-2*complex(0,1)*kk*lam1*TH1x3*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x3*vL*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x3*vL*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x3*vR*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x3*vR*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*kk*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*kk*TH4x3*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x3*vR*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x3*vR*cmath.cos(zeta)*cmath.sin(zeta) + complex(0,1)*kap*TH3x3*cmath.cos(zeta)*cmath.sqrt(2)*cmath.sin(zeta) - 2*alp1*complex(0,1)*kk*TH1x3*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*kk*TH1x3*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x3*vL*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x3*vR*cmath.sin(zeta)**2',
                  order = {'QED':1})

GC_873 = Coupling(name = 'GC_873',
                  value = '-2*complex(0,1)*kk*lam1*TH1x4*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH3x4*vL*cmath.cos(zeta)**2 - 2*alp2*complex(0,1)*TH3x4*vL*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*TH4x4*vR*cmath.cos(zeta)**2 - 2*alp3*complex(0,1)*TH4x4*vR*cmath.cos(zeta)**2 + 2*alp2*complex(0,1)*kk*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*kk*TH4x4*cmath.cos(zeta)*cmath.sin(zeta) + 2*alp2*complex(0,1)*TH1x4*vR*cmath.cos(zeta)*cmath.sin(zeta) - 2*alp3*complex(0,1)*TH1x4*vR*cmath.cos(zeta)*cmath.sin(zeta) + complex(0,1)*kap*TH3x4*cmath.cos(zeta)*cmath.sqrt(2)*cmath.sin(zeta) - 2*alp1*complex(0,1)*kk*TH1x4*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*kk*TH1x4*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*TH3x4*vL*cmath.sin(zeta)**2 - 2*complex(0,1)*lam3*TH4x4*vR*cmath.sin(zeta)**2',
                  order = {'QED':1})

GC_874 = Coupling(name = 'GC_874',
                  value = '-2*complex(0,1)*lam1*cmath.cos(beta)**2*cmath.cos(zeta)**2 - 4*complex(0,1)*lam2*cmath.cos(beta)**2*cmath.cos(zeta)**2 - 2*alp1*complex(0,1)*cmath.cos(zeta)**2*cmath.sin(beta)**2 - 2*alp3*complex(0,1)*cmath.cos(zeta)**2*cmath.sin(beta)**2 - 2*alp1*complex(0,1)*cmath.cos(beta)**2*cmath.sin(zeta)**2 - 2*alp3*complex(0,1)*cmath.cos(beta)**2*cmath.sin(zeta)**2 - 2*complex(0,1)*lam4*cmath.sin(beta)**2*cmath.sin(zeta)**2',
                  order = {'QED':2})

GC_875 = Coupling(name = 'GC_875',
                  value = '-4*complex(0,1)*lam1*cmath.cos(zeta)**4 - 8*alp1*complex(0,1)*cmath.cos(zeta)**2*cmath.sin(zeta)**2 - 8*alp2*complex(0,1)*cmath.cos(zeta)**2*cmath.sin(zeta)**2 - 4*complex(0,1)*lam3*cmath.sin(zeta)**4',
                  order = {'QED':2})

