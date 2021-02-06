# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Fri 21 Jun 2019 18:24:07



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
CKMlam = Parameter(name = 'CKMlam',
                   nature = 'external',
                   type = 'real',
                   value = 0.22453,
                   texname = '\\lambda _{\\text{CKM}}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 1 ])

CKMA = Parameter(name = 'CKMA',
                 nature = 'external',
                 type = 'real',
                 value = 0.836,
                 texname = 'A_{\\text{CKM}}',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 2 ])

CKMrho = Parameter(name = 'CKMrho',
                   nature = 'external',
                   type = 'real',
                   value = 0.122,
                   texname = '\\rho _{\\text{CKM}}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 3 ])

CKMeta = Parameter(name = 'CKMeta',
                   nature = 'external',
                   type = 'real',
                   value = 0.355,
                   texname = '\\eta _{\\text{CKM}}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 4 ])

CKMps12 = Parameter(name = 'CKMps12',
                    nature = 'external',
                    type = 'real',
                    value = 0.22453,
                    texname = '\\text{CKMps12}',
                    lhablock = 'CKMBLOCK',
                    lhacode = [ 11 ])

CKMps23 = Parameter(name = 'CKMps23',
                    nature = 'external',
                    type = 'real',
                    value = 0.0421,
                    texname = '\\text{CKMps23}',
                    lhablock = 'CKMBLOCK',
                    lhacode = [ 12 ])

CKMps13 = Parameter(name = 'CKMps13',
                    nature = 'external',
                    type = 'real',
                    value = 0.00364,
                    texname = '\\text{CKMps13}',
                    lhablock = 'CKMBLOCK',
                    lhacode = [ 13 ])

CKMpdel = Parameter(name = 'CKMpdel',
                    nature = 'external',
                    type = 'real',
                    value = 1.24,
                    texname = '\\text{CKMpdel}',
                    lhablock = 'CKMBLOCK',
                    lhacode = [ 14 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 0.5,
                 texname = '\\lambda _2',
                 lhablock = 'HPOTINPUTS',
                 lhacode = [ 1 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = 1.6,
                 texname = '\\lambda _3',
                 lhablock = 'HPOTINPUTS',
                 lhacode = [ 2 ])

alp1 = Parameter(name = 'alp1',
                 nature = 'external',
                 type = 'real',
                 value = 0.3,
                 texname = '\\alpha _1',
                 lhablock = 'HPOTINPUTS',
                 lhacode = [ 3 ])

alp2 = Parameter(name = 'alp2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\alpha _2',
                 lhablock = 'HPOTINPUTS',
                 lhacode = [ 4 ])

alp3 = Parameter(name = 'alp3',
                 nature = 'external',
                 type = 'real',
                 value = 0.3,
                 texname = '\\alpha _3',
                 lhablock = 'HPOTINPUTS',
                 lhacode = [ 5 ])

kap = Parameter(name = 'kap',
                nature = 'external',
                type = 'real',
                value = -10.,
                texname = '\\kappa',
                lhablock = 'HPOTINPUTS',
                lhacode = [ 6 ])

PMNSs12 = Parameter(name = 'PMNSs12',
                    nature = 'external',
                    type = 'real',
                    value = 0.5449770637375485,
                    texname = '\\text{PMNSs12}',
                    lhablock = 'PMNSBLOCK',
                    lhacode = [ 1 ])

PMNSs23 = Parameter(name = 'PMNSs23',
                    nature = 'external',
                    type = 'real',
                    value = 0.6519202405202649,
                    texname = '\\text{PMNSs23}',
                    lhablock = 'PMNSBLOCK',
                    lhacode = [ 2 ])

PMNSs13 = Parameter(name = 'PMNSs13',
                    nature = 'external',
                    type = 'real',
                    value = 0.14662878298615178,
                    texname = '\\text{PMNSs13}',
                    lhablock = 'PMNSBLOCK',
                    lhacode = [ 3 ])

PMNSdel = Parameter(name = 'PMNSdel',
                    nature = 'external',
                    type = 'real',
                    value = 4.335397861953914,
                    texname = '\\text{PMNSdel}',
                    lhablock = 'PMNSBLOCK',
                    lhacode = [ 4 ])

PMNSps12 = Parameter(name = 'PMNSps12',
                     nature = 'external',
                     type = 'real',
                     value = 0.5449770637375485,
                     texname = '\\text{PMNSps12}',
                     lhablock = 'PMNSBLOCK',
                     lhacode = [ 11 ])

PMNSps23 = Parameter(name = 'PMNSps23',
                     nature = 'external',
                     type = 'real',
                     value = 0.6519202405202649,
                     texname = '\\text{PMNSps23}',
                     lhablock = 'PMNSBLOCK',
                     lhacode = [ 12 ])

PMNSps13 = Parameter(name = 'PMNSps13',
                     nature = 'external',
                     type = 'real',
                     value = 0.14662878298615178,
                     texname = '\\text{PMNSps13}',
                     lhablock = 'PMNSBLOCK',
                     lhacode = [ 13 ])

PMNSpdel = Parameter(name = 'PMNSpdel',
                     nature = 'external',
                     type = 'real',
                     value = 4.335397861953914,
                     texname = '\\text{PMNSpdel}',
                     lhablock = 'PMNSBLOCK',
                     lhacode = [ 14 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{Subsuperscript}[\\alpha ,w,-1]',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 10.,
               texname = 't_{\\beta }',
               lhablock = 'SMINPUTS',
               lhacode = [ 5 ])

gR = Parameter(name = 'gR',
               nature = 'external',
               type = 'real',
               value = 0.64648221,
               texname = 'g_R',
               lhablock = 'SMINPUTS',
               lhacode = [ 6 ])

vevp = Parameter(name = 'vevp',
                 nature = 'external',
                 type = 'real',
                 value = 6500,
                 texname = 'v\'',
                 lhablock = 'SMINPUTS',
                 lhacode = [ 7 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MH0 = Parameter(name = 'MH0',
                nature = 'external',
                type = 'real',
                value = 125.,
                texname = '\\text{MH0}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

Mve = Parameter(name = 'Mve',
                nature = 'external',
                type = 'real',
                value = 1.e-12,
                texname = '\\text{Mve}',
                lhablock = 'MASS',
                lhacode = [ 12 ])

Mvm = Parameter(name = 'Mvm',
                nature = 'external',
                type = 'real',
                value = 8.9e-12,
                texname = '\\text{Mvm}',
                lhablock = 'MASS',
                lhacode = [ 14 ])

Mvt = Parameter(name = 'Mvt',
                nature = 'external',
                type = 'real',
                value = 5.04e-11,
                texname = '\\text{Mvt}',
                lhablock = 'MASS',
                lhacode = [ 16 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Mne = Parameter(name = 'Mne',
                nature = 'external',
                type = 'real',
                value = 300,
                texname = '\\text{Mne}',
                lhablock = 'MASS',
                lhacode = [ 18 ])

Mnm = Parameter(name = 'Mnm',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{Mnm}',
                lhablock = 'MASS',
                lhacode = [ 6000014 ])

Mnt = Parameter(name = 'Mnt',
                nature = 'external',
                type = 'real',
                value = 700,
                texname = '\\text{Mnt}',
                lhablock = 'MASS',
                lhacode = [ 6000016 ])

MDP = Parameter(name = 'MDP',
                nature = 'external',
                type = 'real',
                value = 301,
                texname = '\\text{MDP}',
                lhablock = 'MASS',
                lhacode = [ 6000001 ])

MSP = Parameter(name = 'MSP',
                nature = 'external',
                type = 'real',
                value = 501,
                texname = '\\text{MSP}',
                lhablock = 'MASS',
                lhacode = [ 6000003 ])

MBP = Parameter(name = 'MBP',
                nature = 'external',
                type = 'real',
                value = 701,
                texname = '\\text{MBP}',
                lhablock = 'MASS',
                lhacode = [ 6000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 13.2,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 32 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WWp = Parameter(name = 'WWp',
                nature = 'external',
                type = 'real',
                value = 3.04,
                texname = '\\text{WWp}',
                lhablock = 'DECAY',
                lhacode = [ 34 ])

WH0 = Parameter(name = 'WH0',
                nature = 'external',
                type = 'real',
                value = 0.0176,
                texname = '\\text{WH0}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

WH1 = Parameter(name = 'WH1',
                nature = 'external',
                type = 'real',
                value = 0.95,
                texname = '\\text{WH1}',
                lhablock = 'DECAY',
                lhacode = [ 35 ])

WH2 = Parameter(name = 'WH2',
                nature = 'external',
                type = 'real',
                value = 3.18,
                texname = '\\text{WH2}',
                lhablock = 'DECAY',
                lhacode = [ 45 ])

WH3 = Parameter(name = 'WH3',
                nature = 'external',
                type = 'real',
                value = 781.,
                texname = '\\text{WH3}',
                lhablock = 'DECAY',
                lhacode = [ 55 ])

WA1 = Parameter(name = 'WA1',
                nature = 'external',
                type = 'real',
                value = 0.95,
                texname = '\\text{WA1}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WA2 = Parameter(name = 'WA2',
                nature = 'external',
                type = 'real',
                value = 3.18,
                texname = '\\text{WA2}',
                lhablock = 'DECAY',
                lhacode = [ 46 ])

WHp1 = Parameter(name = 'WHp1',
                 nature = 'external',
                 type = 'real',
                 value = 2.83,
                 texname = '\\text{WHp1}',
                 lhablock = 'DECAY',
                 lhacode = [ 37 ])

WHp2 = Parameter(name = 'WHp2',
                 nature = 'external',
                 type = 'real',
                 value = 0.423,
                 texname = '\\text{WHp2}',
                 lhablock = 'DECAY',
                 lhacode = [ 47 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wnm = Parameter(name = 'Wnm',
                nature = 'external',
                type = 'real',
                value = 0.000709,
                texname = '\\text{Wnm}',
                lhablock = 'DECAY',
                lhacode = [ 6000014 ])

Wnt = Parameter(name = 'Wnt',
                nature = 'external',
                type = 'real',
                value = 1.13,
                texname = '\\text{Wnt}',
                lhablock = 'DECAY',
                lhacode = [ 6000016 ])

WSP = Parameter(name = 'WSP',
                nature = 'external',
                type = 'real',
                value = 0.262,
                texname = '\\text{WSP}',
                lhablock = 'DECAY',
                lhacode = [ 6000003 ])

WBP = Parameter(name = 'WBP',
                nature = 'external',
                type = 'real',
                value = 9.85,
                texname = '\\text{WBP}',
                lhablock = 'DECAY',
                lhacode = [ 6000005 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '1/(2**0.25*cmath.sqrt(Gf))',
                texname = 'v')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (cmath.pi*MZ**2)/(aEWM1*Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MWp = Parameter(name = 'MWp',
                nature = 'internal',
                type = 'real',
                value = '(gR*vevp)/2.',
                texname = 'M_{W\'}')

TH1x2 = Parameter(name = 'TH1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{TH1x2}')

TH2x1 = Parameter(name = 'TH2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{TH2x1}')

TH2x2 = Parameter(name = 'TH2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{TH2x2}')

TH2x3 = Parameter(name = 'TH2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{TH2x3}')

TH2x4 = Parameter(name = 'TH2x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{TH2x4}')

TH3x2 = Parameter(name = 'TH3x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{TH3x2}')

TH4x2 = Parameter(name = 'TH4x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{TH4x2}')

CKMs12 = Parameter(name = 'CKMs12',
                   nature = 'internal',
                   type = 'real',
                   value = 'CKMlam',
                   texname = '\\text{CKMs12}')

CKMs23 = Parameter(name = 'CKMs23',
                   nature = 'internal',
                   type = 'real',
                   value = 'CKMA*CKMlam**2',
                   texname = '\\text{CKMs23}')

CKMs13d = Parameter(name = 'CKMs13d',
                    nature = 'internal',
                    type = 'complex',
                    value = '(CKMA*CKMlam**3*(CKMrho + CKMeta*complex(0,1))*cmath.sqrt(1 - CKMA**2*CKMlam**4))/((1 - CKMA**2*CKMlam**4*(CKMrho + CKMeta*complex(0,1)))*cmath.sqrt(1 - CKMlam**2))',
                    texname = '\\text{CKMs13d}')

PMNSs13d = Parameter(name = 'PMNSs13d',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSs13*cmath.exp(complex(0,1)*PMNSdel)',
                     texname = '\\text{PMNSs13d}')

PMNSc12 = Parameter(name = 'PMNSc12',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(1 - PMNSs12**2)',
                    texname = '\\text{PMNSc12}')

PMNSc13 = Parameter(name = 'PMNSc13',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(1 - PMNSs13**2)',
                    texname = '\\text{PMNSc13}')

PMNSc23 = Parameter(name = 'PMNSc23',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(1 - PMNSs23**2)',
                    texname = '\\text{PMNSc23}')

PMNSps13d = Parameter(name = 'PMNSps13d',
                      nature = 'internal',
                      type = 'complex',
                      value = 'PMNSps13*cmath.exp(complex(0,1)*PMNSpdel)',
                      texname = '\\text{PMNSps13d}')

PMNSpc12 = Parameter(name = 'PMNSpc12',
                     nature = 'internal',
                     type = 'real',
                     value = 'cmath.sqrt(1 - PMNSps12**2)',
                     texname = '\\text{PMNSpc12}')

PMNSpc13 = Parameter(name = 'PMNSpc13',
                     nature = 'internal',
                     type = 'real',
                     value = 'cmath.sqrt(1 - PMNSps13**2)',
                     texname = '\\text{PMNSpc13}')

PMNSpc23 = Parameter(name = 'PMNSpc23',
                     nature = 'internal',
                     type = 'real',
                     value = 'cmath.sqrt(1 - PMNSps23**2)',
                     texname = '\\text{PMNSpc23}')

CKMps13d = Parameter(name = 'CKMps13d',
                     nature = 'internal',
                     type = 'complex',
                     value = 'CKMps13*cmath.exp(CKMpdel*complex(0,1))',
                     texname = '\\text{CKMps13d}')

CKMpc12 = Parameter(name = 'CKMpc12',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(1 - CKMps12**2)',
                    texname = '\\text{CKMpc12}')

CKMpc13 = Parameter(name = 'CKMpc13',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(1 - CKMps13**2)',
                    texname = '\\text{CKMpc13}')

CKMpc23 = Parameter(name = 'CKMpc23',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(1 - CKMps23**2)',
                    texname = '\\text{CKMpc23}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMs13d',
                   texname = '\\text{CKM1x3}')

CKMc12 = Parameter(name = 'CKMc12',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(1 - CKMs12**2)',
                   texname = '\\text{CKMc12}')

CKMc13 = Parameter(name = 'CKMc13',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(1 - abs(CKMs13d)**2)',
                   texname = '\\text{CKMc13}')

CKMc23 = Parameter(name = 'CKMc23',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(1 - CKMs23**2)',
                   texname = '\\text{CKMc23}')

CKMp1x1 = Parameter(name = 'CKMp1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKMpc12*CKMpc13',
                    texname = '\\text{CKMp1x1}')

CKMp1x2 = Parameter(name = 'CKMp1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKMpc13*CKMps12',
                    texname = '\\text{CKMp1x2}')

CKMp1x3 = Parameter(name = 'CKMp1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKMps13d',
                    texname = '\\text{CKMp1x3}')

CKMp2x1 = Parameter(name = 'CKMp2x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(CKMpc23*CKMps12) - CKMpc12*CKMps13d*CKMps23',
                    texname = '\\text{CKMp2x1}')

CKMp2x2 = Parameter(name = 'CKMp2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKMpc12*CKMpc23 - CKMps12*CKMps13d*CKMps23',
                    texname = '\\text{CKMp2x2}')

CKMp2x3 = Parameter(name = 'CKMp2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKMpc13*CKMps23',
                    texname = '\\text{CKMp2x3}')

CKMp3x1 = Parameter(name = 'CKMp3x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(CKMpc12*CKMpc23*CKMps13d) + CKMps12*CKMps23',
                    texname = '\\text{CKMp3x1}')

CKMp3x2 = Parameter(name = 'CKMp3x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(CKMpc23*CKMps12*CKMps13d) - CKMpc12*CKMps23',
                    texname = '\\text{CKMp3x2}')

CKMp3x3 = Parameter(name = 'CKMp3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'CKMpc13*CKMpc23',
                    texname = '\\text{CKMp3x3}')

PMNS1x1 = Parameter(name = 'PMNS1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'PMNSc12*PMNSc13',
                    texname = '\\text{PMNS1x1}')

PMNS1x2 = Parameter(name = 'PMNS1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'PMNSc13*PMNSs12',
                    texname = '\\text{PMNS1x2}')

PMNS1x3 = Parameter(name = 'PMNS1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'PMNSs13d',
                    texname = '\\text{PMNS1x3}')

PMNS2x1 = Parameter(name = 'PMNS2x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(PMNSc23*PMNSs12) - PMNSc12*PMNSs13d*PMNSs23',
                    texname = '\\text{PMNS2x1}')

PMNS2x2 = Parameter(name = 'PMNS2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'PMNSc12*PMNSc23 - PMNSs12*PMNSs13d*PMNSs23',
                    texname = '\\text{PMNS2x2}')

PMNS2x3 = Parameter(name = 'PMNS2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'PMNSc13*PMNSs23',
                    texname = '\\text{PMNS2x3}')

PMNS3x1 = Parameter(name = 'PMNS3x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(PMNSc12*PMNSc23*PMNSs13d) + PMNSs12*PMNSs23',
                    texname = '\\text{PMNS3x1}')

PMNS3x2 = Parameter(name = 'PMNS3x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(PMNSc23*PMNSs12*PMNSs13d) - PMNSc12*PMNSs23',
                    texname = '\\text{PMNS3x2}')

PMNS3x3 = Parameter(name = 'PMNS3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'PMNSc13*PMNSc23',
                    texname = '\\text{PMNS3x3}')

PMNSp1x1 = Parameter(name = 'PMNSp1x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSpc12*PMNSpc13',
                     texname = '\\text{PMNSp1x1}')

PMNSp1x2 = Parameter(name = 'PMNSp1x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSpc13*PMNSps12',
                     texname = '\\text{PMNSp1x2}')

PMNSp1x3 = Parameter(name = 'PMNSp1x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSps13d',
                     texname = '\\text{PMNSp1x3}')

PMNSp2x1 = Parameter(name = 'PMNSp2x1',
                     nature = 'internal',
                     type = 'complex',
                     value = '-(PMNSpc23*PMNSps12) - PMNSpc12*PMNSps13d*PMNSps23',
                     texname = '\\text{PMNSp2x1}')

PMNSp2x2 = Parameter(name = 'PMNSp2x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSpc12*PMNSpc23 - PMNSps12*PMNSps13d*PMNSps23',
                     texname = '\\text{PMNSp2x2}')

PMNSp2x3 = Parameter(name = 'PMNSp2x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSpc13*PMNSps23',
                     texname = '\\text{PMNSp2x3}')

PMNSp3x1 = Parameter(name = 'PMNSp3x1',
                     nature = 'internal',
                     type = 'complex',
                     value = '-(PMNSpc12*PMNSpc23*PMNSps13d) + PMNSps12*PMNSps23',
                     texname = '\\text{PMNSp3x1}')

PMNSp3x2 = Parameter(name = 'PMNSp3x2',
                     nature = 'internal',
                     type = 'complex',
                     value = '-(PMNSpc23*PMNSps12*PMNSps13d) - PMNSpc12*PMNSps23',
                     texname = '\\text{PMNSp3x2}')

PMNSp3x3 = Parameter(name = 'PMNSp3x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNSpc13*PMNSpc23',
                     texname = '\\text{PMNSp3x3}')

gL = Parameter(name = 'gL',
               nature = 'internal',
               type = 'real',
               value = '(2*MW)/vev',
               texname = 'g_L')

kk = Parameter(name = 'kk',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'k')

vL = Parameter(name = 'vL',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_L')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMc12*CKMc13',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMc13*CKMs12',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMc23*CKMs12) - CKMc12*CKMs13d*CKMs23',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMc12*CKMc23 - CKMs12*CKMs13d*CKMs23',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMc13*CKMs23',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMc12*CKMc23*CKMs13d) + CKMs12*CKMs23',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMc23*CKMs12*CKMs13d) - CKMc12*CKMs23',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMc13*CKMc23',
                   texname = '\\text{CKM3x3}')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'ee/gL',
               texname = 's_w')

vR = Parameter(name = 'vR',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(-kk**2 + vevp**2)',
               texname = 'v_R')

yd1x1 = Parameter(name = 'yd1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '(MD*cmath.sqrt(2))/vL',
                  texname = '\\text{yd1x1}')

yd2x2 = Parameter(name = 'yd2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '(MS*cmath.sqrt(2))/vL',
                  texname = '\\text{yd2x2}')

yd3x3 = Parameter(name = 'yd3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(MB*cmath.sqrt(2))/vL',
                  texname = '\\text{yd3x3}')

ye1x1 = Parameter(name = 'ye1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '(Me*cmath.sqrt(2))/kk',
                  texname = '\\text{ye1x1}')

ye2x2 = Parameter(name = 'ye2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '(MMU*cmath.sqrt(2))/kk',
                  texname = '\\text{ye2x2}')

ye3x3 = Parameter(name = 'ye3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(MTA*cmath.sqrt(2))/kk',
                  texname = '\\text{ye3x3}')

ynu1x1 = Parameter(name = 'ynu1x1',
                   nature = 'internal',
                   type = 'real',
                   value = '(Mve*cmath.sqrt(2))/vL',
                   texname = '\\text{ynu1x1}')

ynu2x2 = Parameter(name = 'ynu2x2',
                   nature = 'internal',
                   type = 'real',
                   value = '(Mvm*cmath.sqrt(2))/vL',
                   texname = '\\text{ynu2x2}')

ynu3x3 = Parameter(name = 'ynu3x3',
                   nature = 'internal',
                   type = 'real',
                   value = '(Mvt*cmath.sqrt(2))/vL',
                   texname = '\\text{ynu3x3}')

yu1x1 = Parameter(name = 'yu1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '(MU*cmath.sqrt(2))/kk',
                  texname = '\\text{yu1x1}')

yu2x2 = Parameter(name = 'yu2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '(MC*cmath.sqrt(2))/kk',
                  texname = '\\text{yu2x2}')

yu3x3 = Parameter(name = 'yu3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(MT*cmath.sqrt(2))/kk',
                  texname = '\\text{yu3x3}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw**2)',
               texname = 'c_w')

MA1 = Parameter(name = 'MA1',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(2*kk**2*lam2 - (alp2 - alp3)*(vL**2 + vR**2) - (kap*vL*vR)/(kk*cmath.sqrt(2)))',
                texname = '\\text{MA1}')

MA2 = Parameter(name = 'MA2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(-((kap*(vL**2*vR**2 + kk**2*(vL**2 + vR**2)))/(kk*vL*vR)))/2**0.25',
                texname = '\\text{MA2}')

MH1 = Parameter(name = 'MH1',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(2*kk**2*lam2 - (alp2 - alp3)*(vL**2 + vR**2) - (kap*vL*vR)/(kk*cmath.sqrt(2)))',
                texname = '\\text{MH1}')

MHp1 = Parameter(name = 'MHp1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(-(((kk**2 + vL**2)*(2*(alp2 - alp3)*kk*vL + kap*vR*cmath.sqrt(2)))/(kk*vL)))/cmath.sqrt(2)',
                 texname = '\\text{MHp1}')

MHp2 = Parameter(name = 'MHp2',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(-(((kk**2 + vR**2)*(2*(alp2 - alp3)*kk*vR + kap*vL*cmath.sqrt(2)))/(kk*vR)))/cmath.sqrt(2)',
                 texname = '\\text{MHp2}')

MU22 = Parameter(name = 'MU22',
                 nature = 'internal',
                 type = 'real',
                 value = '(alp1 + alp2)*kk**2 + lam3*(vL**2 + vR**2)',
                 texname = '\\text{Subsuperscript}[\\mu ,2,2]')

TH1x1 = Parameter(name = 'TH1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*cmath.sqrt(1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH1x1}')

TH3x1 = Parameter(name = 'TH3x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '(vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*cmath.sqrt(1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH3x1}')

TH4x1 = Parameter(name = 'TH4x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '1/cmath.sqrt(1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2))',
                  texname = '\\text{TH4x1}')

tz = Parameter(name = 'tz',
               nature = 'internal',
               type = 'real',
               value = 'kk/vR',
               texname = 't_{\\zeta }')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(-4*(alp1 + alp2)**2*kap*kk**4*(vL**2 - vR**2)**2 + kk*MH0**6*vL*vR*cmath.sqrt(2) - 2*MH0**2*(kap*(lam3*vL**2*vR**2*(vL**2 + vR**2) + kk**2*(4*(alp1 + alp2)*vL**2*vR**2 + lam3*(vL**2 - vR**2)**2)) + 2*(alp1 + alp2)**2*kk**3*vL*vR*(vL**2 + vR**2)*cmath.sqrt(2)) + MH0**4*(kap*(vL**2*vR**2 + kk**2*(vL**2 + vR**2)) - 2*kk*lam3*vL*vR*(vL**2 + vR**2)*cmath.sqrt(2)))/(-4*kap*kk**4*lam3*(vL**2 - vR**2)**2 + 2*kk**3*MH0**4*vL*vR*cmath.sqrt(2) + 2*kk**3*MH0**2*(vL**2 + vR**2)*(kap*kk - 2*lam3*vL*vR*cmath.sqrt(2)))',
                 texname = '\\lambda _1')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'real',
                 value = 'lam3 - (kap*kk)/(vL*vR*cmath.sqrt(2))',
                 texname = '\\lambda _4')

ydp1x1 = Parameter(name = 'ydp1x1',
                   nature = 'internal',
                   type = 'real',
                   value = '(MDP*cmath.sqrt(2))/vR',
                   texname = '\\text{ydp1x1}')

ydp2x2 = Parameter(name = 'ydp2x2',
                   nature = 'internal',
                   type = 'real',
                   value = '(MSP*cmath.sqrt(2))/vR',
                   texname = '\\text{ydp2x2}')

ydp3x3 = Parameter(name = 'ydp3x3',
                   nature = 'internal',
                   type = 'real',
                   value = '(MBP*cmath.sqrt(2))/vR',
                   texname = '\\text{ydp3x3}')

yn1x1 = Parameter(name = 'yn1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '(Mne*cmath.sqrt(2))/vR',
                  texname = '\\text{yn1x1}')

yn2x2 = Parameter(name = 'yn2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '(Mnm*cmath.sqrt(2))/vR',
                  texname = '\\text{yn2x2}')

yn3x3 = Parameter(name = 'yn3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(Mnt*cmath.sqrt(2))/vR',
                  texname = '\\text{yn3x3}')

MH2 = Parameter(name = 'MH2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(-MH0**2 + (vL*vR*(-(kap*vL*vR) + 2*kk**3*lam1*cmath.sqrt(2)) + kk*(vL**2 + vR**2)*(-(kap*kk) + 2*lam3*vL*vR*cmath.sqrt(2)))/(kk*vL*vR*cmath.sqrt(2)) - cmath.sqrt((-MH0**2 + (vL*vR*(-(kap*vL*vR) + 2*kk**3*lam1*cmath.sqrt(2)) + kk*(vL**2 + vR**2)*(-(kap*kk) + 2*lam3*vL*vR*cmath.sqrt(2)))/(kk*vL*vR*cmath.sqrt(2)))**2 + 4*((kap*kk**2*(4*(alp1 + alp2)*vL**2*vR**2 + lam3*(vL**2 - vR**2)**2)*cmath.sqrt(2) + (vL**2 + vR**2)*(4*kk**3*(alp1**2 + 2*alp1*alp2 + alp2**2 - lam1*lam3)*vL*vR + kap*(kk**4*lam1 + lam3*vL**2*vR**2)*cmath.sqrt(2)))/(kk*vL*vR) + MH0**2*(-MH0**2 + (vL*vR*(-(kap*vL*vR) + 2*kk**3*lam1*cmath.sqrt(2)) + kk*(vL**2 + vR**2)*(-(kap*kk) + 2*lam3*vL*vR*cmath.sqrt(2)))/(kk*vL*vR*cmath.sqrt(2))))))/cmath.sqrt(2)',
                texname = 'M_{\\text{H2}}')

MH3 = Parameter(name = 'MH3',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(-MH0**2 + (vL*vR*(-(kap*vL*vR) + 2*kk**3*lam1*cmath.sqrt(2)) + kk*(vL**2 + vR**2)*(-(kap*kk) + 2*lam3*vL*vR*cmath.sqrt(2)))/(kk*vL*vR*cmath.sqrt(2)) + cmath.sqrt((-MH0**2 + (vL*vR*(-(kap*vL*vR) + 2*kk**3*lam1*cmath.sqrt(2)) + kk*(vL**2 + vR**2)*(-(kap*kk) + 2*lam3*vL*vR*cmath.sqrt(2)))/(kk*vL*vR*cmath.sqrt(2)))**2 + 4*((kap*kk**2*(4*(alp1 + alp2)*vL**2*vR**2 + lam3*(vL**2 - vR**2)**2)*cmath.sqrt(2) + (vL**2 + vR**2)*(4*kk**3*(alp1**2 + 2*alp1*alp2 + alp2**2 - lam1*lam3)*vL*vR + kap*(kk**4*lam1 + lam3*vL**2*vR**2)*cmath.sqrt(2)))/(kk*vL*vR) + MH0**2*(-MH0**2 + (vL*vR*(-(kap*vL*vR) + 2*kk**3*lam1*cmath.sqrt(2)) + kk*(vL**2 + vR**2)*(-(kap*kk) + 2*lam3*vL*vR*cmath.sqrt(2)))/(kk*vL*vR*cmath.sqrt(2))))))/cmath.sqrt(2)',
                texname = 'M_{\\text{H3}}')

MU12 = Parameter(name = 'MU12',
                 nature = 'internal',
                 type = 'real',
                 value = 'kk**2*lam1 + (alp1 + alp2)*(vL**2 + vR**2) + (kap*vL*vR)/(kk*cmath.sqrt(2))',
                 texname = '\\text{Subsuperscript}[\\mu ,1,2]')

zeta = Parameter(name = 'zeta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tz)',
                 texname = '\\zeta')

Ghaa = Parameter(name = 'Ghaa',
                 nature = 'internal',
                 type = 'real',
                 value = '(47*ee**2*TH1x1*csc(beta))/(62.*cmath.pi**2*vev)',
                 texname = 'g_{\\text{haa}}')

Ghgg = Parameter(name = 'Ghgg',
                 nature = 'internal',
                 type = 'real',
                 value = '-(aS*TH1x1*csc(beta))/(3.*cmath.pi*vev)',
                 texname = 'g_{\\text{hgg}}')

gY = Parameter(name = 'gY',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_Y')

sph = Parameter(name = 'sph',
                nature = 'internal',
                type = 'real',
                value = 'gY/gR',
                texname = 's_p')

TH1x3 = Parameter(name = 'TH1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))/cmath.sqrt((1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2))*(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + ((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))**2 - (2*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH1x3}')

TH1x4 = Parameter(name = 'TH1x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '((-((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))*((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(-((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(abs((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(-((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))*cmath.sqrt(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + ((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))**2 - (2*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH1x4}')

TH3x3 = Parameter(name = 'TH3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(1 + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))/cmath.sqrt((1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2))*(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + ((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))**2 - (2*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH3x3}')

TH3x4 = Parameter(name = 'TH3x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '(((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))*((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(-((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(abs((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(-((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))*cmath.sqrt(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + ((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))**2 - (2*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH3x4}')

TH4x3 = Parameter(name = 'TH4x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) - ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) - (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))/cmath.sqrt((1 + (2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2))*(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + ((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))**2 - (2*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH4x3}')

TH4x4 = Parameter(name = 'TH4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '(((vL*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))*((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(-((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(abs((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(-((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))) + (2*MH3**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH3**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH3**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))*cmath.sqrt(((2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2) + ((vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) - (vL*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))))**2 - (2*(2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(2*MH2**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH2**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2))))))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))) + ((2*MH0**4*vL*vR - 2*kap*kk*lam3*(vL**2 - vR**2)**2*cmath.sqrt(2) + MH0**2*(vL**2 + vR**2)*(-4*lam3*vL*vR + kap*kk*cmath.sqrt(2)))**2*(1 + (vL**2*(2*kap*(vL**2 - vR**2)*((alp1 + alp2)*kk**2 + lam3*vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vR**2*cmath.sqrt(2)))**2)/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH2**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))/(vR**2*(2*kap*((alp1 + alp2)*kk**2 + lam3*vL**2)*(-vL**2 + vR**2)*cmath.sqrt(2) + MH0**2*(4*(alp1 + alp2)*kk*vL*vR + kap*vL**2*cmath.sqrt(2)))**2)))',
                  texname = '\\text{TH4x4}')

gBL = Parameter(name = 'gBL',
                nature = 'internal',
                type = 'real',
                value = '(gR*gY)/cmath.sqrt(gR**2 - gY**2)',
                texname = 'g_{B-L}')

cph = Parameter(name = 'cph',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - sph**2)',
                texname = 'c_p')

MZp = Parameter(name = 'MZp',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(gBL**2*sph**2*vL**2 + (gR**2*(cph**4*kk**2 + vR**2))/cph**2)/2.',
                texname = 'M_{Z\'}')

t2t = Parameter(name = 't2t',
                nature = 'internal',
                type = 'real',
                value = '(2*cph*cw*gL*gR*(cph**2*kk**2 - sph**2*vL**2))/(-(cph**2*(gL**2 - cph**2*cw**2*gR**2)*kk**2) - cph**2*gL**2*(gL**2 - cw**2*gBL**2*sph**2) + cw**2*gR**2*vR**2)',
                texname = 't_{2 \\theta }')

st = Parameter(name = 'st',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(cmath.atan(t2t)/2.)',
               texname = 's_t')

ct = Parameter(name = 'ct',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - st**2)',
               texname = 'c_t')

I1b11 = Parameter(name = 'I1b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd1x1',
                  texname = '\\text{I1b11}')

I1b12 = Parameter(name = 'I1b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yd2x2',
                  texname = '\\text{I1b12}')

I1b13 = Parameter(name = 'I1b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yd3x3',
                  texname = '\\text{I1b13}')

I1b21 = Parameter(name = 'I1b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd1x1',
                  texname = '\\text{I1b21}')

I1b22 = Parameter(name = 'I1b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yd2x2',
                  texname = '\\text{I1b22}')

I1b23 = Parameter(name = 'I1b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yd3x3',
                  texname = '\\text{I1b23}')

I1b31 = Parameter(name = 'I1b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yd1x1',
                  texname = '\\text{I1b31}')

I1b32 = Parameter(name = 'I1b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yd2x2',
                  texname = '\\text{I1b32}')

I1b33 = Parameter(name = 'I1b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yd3x3',
                  texname = '\\text{I1b33}')

I10b11 = Parameter(name = 'I10b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x1*ye1x1',
                   texname = '\\text{I10b11}')

I10b12 = Parameter(name = 'I10b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x2*ye1x1',
                   texname = '\\text{I10b12}')

I10b13 = Parameter(name = 'I10b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x3*ye1x1',
                   texname = '\\text{I10b13}')

I10b21 = Parameter(name = 'I10b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS2x1*ye2x2',
                   texname = '\\text{I10b21}')

I10b22 = Parameter(name = 'I10b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS2x2*ye2x2',
                   texname = '\\text{I10b22}')

I10b23 = Parameter(name = 'I10b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS2x3*ye2x2',
                   texname = '\\text{I10b23}')

I10b31 = Parameter(name = 'I10b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS3x1*ye3x3',
                   texname = '\\text{I10b31}')

I10b32 = Parameter(name = 'I10b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS3x2*ye3x3',
                   texname = '\\text{I10b32}')

I10b33 = Parameter(name = 'I10b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS3x3*ye3x3',
                   texname = '\\text{I10b33}')

I11b11 = Parameter(name = 'I11b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x1*ynu1x1',
                   texname = '\\text{I11b11}')

I11b12 = Parameter(name = 'I11b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x2*ynu2x2',
                   texname = '\\text{I11b12}')

I11b13 = Parameter(name = 'I11b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x3*ynu3x3',
                   texname = '\\text{I11b13}')

I11b21 = Parameter(name = 'I11b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS2x1*ynu1x1',
                   texname = '\\text{I11b21}')

I11b22 = Parameter(name = 'I11b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS2x2*ynu2x2',
                   texname = '\\text{I11b22}')

I11b23 = Parameter(name = 'I11b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS2x3*ynu3x3',
                   texname = '\\text{I11b23}')

I11b31 = Parameter(name = 'I11b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS3x1*ynu1x1',
                   texname = '\\text{I11b31}')

I11b32 = Parameter(name = 'I11b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS3x2*ynu2x2',
                   texname = '\\text{I11b32}')

I11b33 = Parameter(name = 'I11b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS3x3*ynu3x3',
                   texname = '\\text{I11b33}')

I12b11 = Parameter(name = 'I12b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I12b11}')

I12b12 = Parameter(name = 'I12b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd1x1*complexconjugate(CKM2x1)',
                   texname = '\\text{I12b12}')

I12b13 = Parameter(name = 'I12b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd1x1*complexconjugate(CKM3x1)',
                   texname = '\\text{I12b13}')

I12b21 = Parameter(name = 'I12b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd2x2*complexconjugate(CKM1x2)',
                   texname = '\\text{I12b21}')

I12b22 = Parameter(name = 'I12b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I12b22}')

I12b23 = Parameter(name = 'I12b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd2x2*complexconjugate(CKM3x2)',
                   texname = '\\text{I12b23}')

I12b31 = Parameter(name = 'I12b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM1x3)',
                   texname = '\\text{I12b31}')

I12b32 = Parameter(name = 'I12b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM2x3)',
                   texname = '\\text{I12b32}')

I12b33 = Parameter(name = 'I12b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I12b33}')

I13b11 = Parameter(name = 'I13b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(CKM1x1)',
                   texname = '\\text{I13b11}')

I13b12 = Parameter(name = 'I13b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(CKM2x1)',
                   texname = '\\text{I13b12}')

I13b13 = Parameter(name = 'I13b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I13b13}')

I13b21 = Parameter(name = 'I13b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(CKM1x2)',
                   texname = '\\text{I13b21}')

I13b22 = Parameter(name = 'I13b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(CKM2x2)',
                   texname = '\\text{I13b22}')

I13b23 = Parameter(name = 'I13b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I13b23}')

I13b31 = Parameter(name = 'I13b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(CKM1x3)',
                   texname = '\\text{I13b31}')

I13b32 = Parameter(name = 'I13b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(CKM2x3)',
                   texname = '\\text{I13b32}')

I13b33 = Parameter(name = 'I13b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I13b33}')

I14b11 = Parameter(name = 'I14b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x1*yu1x1*complexconjugate(CKM1x1) + CKMp2x1*yu2x2*complexconjugate(CKM2x1) + CKMp3x1*yu3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I14b11}')

I14b12 = Parameter(name = 'I14b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x2*yu1x1*complexconjugate(CKM1x1) + CKMp2x2*yu2x2*complexconjugate(CKM2x1) + CKMp3x2*yu3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I14b12}')

I14b13 = Parameter(name = 'I14b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x3*yu1x1*complexconjugate(CKM1x1) + CKMp2x3*yu2x2*complexconjugate(CKM2x1) + CKMp3x3*yu3x3*complexconjugate(CKM3x1)',
                   texname = '\\text{I14b13}')

I14b21 = Parameter(name = 'I14b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x1*yu1x1*complexconjugate(CKM1x2) + CKMp2x1*yu2x2*complexconjugate(CKM2x2) + CKMp3x1*yu3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I14b21}')

I14b22 = Parameter(name = 'I14b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x2*yu1x1*complexconjugate(CKM1x2) + CKMp2x2*yu2x2*complexconjugate(CKM2x2) + CKMp3x2*yu3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I14b22}')

I14b23 = Parameter(name = 'I14b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x3*yu1x1*complexconjugate(CKM1x2) + CKMp2x3*yu2x2*complexconjugate(CKM2x2) + CKMp3x3*yu3x3*complexconjugate(CKM3x2)',
                   texname = '\\text{I14b23}')

I14b31 = Parameter(name = 'I14b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x1*yu1x1*complexconjugate(CKM1x3) + CKMp2x1*yu2x2*complexconjugate(CKM2x3) + CKMp3x1*yu3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I14b31}')

I14b32 = Parameter(name = 'I14b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x2*yu1x1*complexconjugate(CKM1x3) + CKMp2x2*yu2x2*complexconjugate(CKM2x3) + CKMp3x2*yu3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I14b32}')

I14b33 = Parameter(name = 'I14b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMp1x3*yu1x1*complexconjugate(CKM1x3) + CKMp2x3*yu2x2*complexconjugate(CKM2x3) + CKMp3x3*yu3x3*complexconjugate(CKM3x3)',
                   texname = '\\text{I14b33}')

I15b11 = Parameter(name = 'I15b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp1x1*complexconjugate(CKMp1x1)',
                   texname = '\\text{I15b11}')

I15b12 = Parameter(name = 'I15b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp1x1*complexconjugate(CKMp2x1)',
                   texname = '\\text{I15b12}')

I15b13 = Parameter(name = 'I15b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp1x1*complexconjugate(CKMp3x1)',
                   texname = '\\text{I15b13}')

I15b21 = Parameter(name = 'I15b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp2x2*complexconjugate(CKMp1x2)',
                   texname = '\\text{I15b21}')

I15b22 = Parameter(name = 'I15b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp2x2*complexconjugate(CKMp2x2)',
                   texname = '\\text{I15b22}')

I15b23 = Parameter(name = 'I15b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp2x2*complexconjugate(CKMp3x2)',
                   texname = '\\text{I15b23}')

I15b31 = Parameter(name = 'I15b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp3x3*complexconjugate(CKMp1x3)',
                   texname = '\\text{I15b31}')

I15b32 = Parameter(name = 'I15b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp3x3*complexconjugate(CKMp2x3)',
                   texname = '\\text{I15b32}')

I15b33 = Parameter(name = 'I15b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ydp3x3*complexconjugate(CKMp3x3)',
                   texname = '\\text{I15b33}')

I16b11 = Parameter(name = 'I16b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(CKMp1x1)',
                   texname = '\\text{I16b11}')

I16b12 = Parameter(name = 'I16b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(CKMp2x1)',
                   texname = '\\text{I16b12}')

I16b13 = Parameter(name = 'I16b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(CKMp3x1)',
                   texname = '\\text{I16b13}')

I16b21 = Parameter(name = 'I16b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(CKMp1x2)',
                   texname = '\\text{I16b21}')

I16b22 = Parameter(name = 'I16b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(CKMp2x2)',
                   texname = '\\text{I16b22}')

I16b23 = Parameter(name = 'I16b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(CKMp3x2)',
                   texname = '\\text{I16b23}')

I16b31 = Parameter(name = 'I16b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(CKMp1x3)',
                   texname = '\\text{I16b31}')

I16b32 = Parameter(name = 'I16b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(CKMp2x3)',
                   texname = '\\text{I16b32}')

I16b33 = Parameter(name = 'I16b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(CKMp3x3)',
                   texname = '\\text{I16b33}')

I17b11 = Parameter(name = 'I17b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x1*ye1x1*complexconjugate(PMNSp1x1) + PMNS2x1*ye2x2*complexconjugate(PMNSp2x1) + PMNS3x1*ye3x3*complexconjugate(PMNSp3x1)',
                   texname = '\\text{I17b11}')

I17b12 = Parameter(name = 'I17b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x2*ye1x1*complexconjugate(PMNSp1x1) + PMNS2x2*ye2x2*complexconjugate(PMNSp2x1) + PMNS3x2*ye3x3*complexconjugate(PMNSp3x1)',
                   texname = '\\text{I17b12}')

I17b13 = Parameter(name = 'I17b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x3*ye1x1*complexconjugate(PMNSp1x1) + PMNS2x3*ye2x2*complexconjugate(PMNSp2x1) + PMNS3x3*ye3x3*complexconjugate(PMNSp3x1)',
                   texname = '\\text{I17b13}')

I17b21 = Parameter(name = 'I17b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x1*ye1x1*complexconjugate(PMNSp1x2) + PMNS2x1*ye2x2*complexconjugate(PMNSp2x2) + PMNS3x1*ye3x3*complexconjugate(PMNSp3x2)',
                   texname = '\\text{I17b21}')

I17b22 = Parameter(name = 'I17b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x2*ye1x1*complexconjugate(PMNSp1x2) + PMNS2x2*ye2x2*complexconjugate(PMNSp2x2) + PMNS3x2*ye3x3*complexconjugate(PMNSp3x2)',
                   texname = '\\text{I17b22}')

I17b23 = Parameter(name = 'I17b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x3*ye1x1*complexconjugate(PMNSp1x2) + PMNS2x3*ye2x2*complexconjugate(PMNSp2x2) + PMNS3x3*ye3x3*complexconjugate(PMNSp3x2)',
                   texname = '\\text{I17b23}')

I17b31 = Parameter(name = 'I17b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x1*ye1x1*complexconjugate(PMNSp1x3) + PMNS2x1*ye2x2*complexconjugate(PMNSp2x3) + PMNS3x1*ye3x3*complexconjugate(PMNSp3x3)',
                   texname = '\\text{I17b31}')

I17b32 = Parameter(name = 'I17b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x2*ye1x1*complexconjugate(PMNSp1x3) + PMNS2x2*ye2x2*complexconjugate(PMNSp2x3) + PMNS3x2*ye3x3*complexconjugate(PMNSp3x3)',
                   texname = '\\text{I17b32}')

I17b33 = Parameter(name = 'I17b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'PMNS1x3*ye1x1*complexconjugate(PMNSp1x3) + PMNS2x3*ye2x2*complexconjugate(PMNSp2x3) + PMNS3x3*ye3x3*complexconjugate(PMNSp3x3)',
                   texname = '\\text{I17b33}')

I18b11 = Parameter(name = 'I18b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye1x1*complexconjugate(PMNSp1x1)',
                   texname = '\\text{I18b11}')

I18b12 = Parameter(name = 'I18b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye2x2*complexconjugate(PMNSp2x1)',
                   texname = '\\text{I18b12}')

I18b13 = Parameter(name = 'I18b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(PMNSp3x1)',
                   texname = '\\text{I18b13}')

I18b21 = Parameter(name = 'I18b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye1x1*complexconjugate(PMNSp1x2)',
                   texname = '\\text{I18b21}')

I18b22 = Parameter(name = 'I18b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye2x2*complexconjugate(PMNSp2x2)',
                   texname = '\\text{I18b22}')

I18b23 = Parameter(name = 'I18b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(PMNSp3x2)',
                   texname = '\\text{I18b23}')

I18b31 = Parameter(name = 'I18b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye1x1*complexconjugate(PMNSp1x3)',
                   texname = '\\text{I18b31}')

I18b32 = Parameter(name = 'I18b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye2x2*complexconjugate(PMNSp2x3)',
                   texname = '\\text{I18b32}')

I18b33 = Parameter(name = 'I18b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(PMNSp3x3)',
                   texname = '\\text{I18b33}')

I19b11 = Parameter(name = 'I19b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn1x1*complexconjugate(PMNSp1x1)',
                   texname = '\\text{I19b11}')

I19b12 = Parameter(name = 'I19b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn1x1*complexconjugate(PMNSp2x1)',
                   texname = '\\text{I19b12}')

I19b13 = Parameter(name = 'I19b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn1x1*complexconjugate(PMNSp3x1)',
                   texname = '\\text{I19b13}')

I19b21 = Parameter(name = 'I19b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn2x2*complexconjugate(PMNSp1x2)',
                   texname = '\\text{I19b21}')

I19b22 = Parameter(name = 'I19b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn2x2*complexconjugate(PMNSp2x2)',
                   texname = '\\text{I19b22}')

I19b23 = Parameter(name = 'I19b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn2x2*complexconjugate(PMNSp3x2)',
                   texname = '\\text{I19b23}')

I19b31 = Parameter(name = 'I19b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn3x3*complexconjugate(PMNSp1x3)',
                   texname = '\\text{I19b31}')

I19b32 = Parameter(name = 'I19b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn3x3*complexconjugate(PMNSp2x3)',
                   texname = '\\text{I19b32}')

I19b33 = Parameter(name = 'I19b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yn3x3*complexconjugate(PMNSp3x3)',
                   texname = '\\text{I19b33}')

I2b11 = Parameter(name = 'I2b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu1x1',
                  texname = '\\text{I2b11}')

I2b12 = Parameter(name = 'I2b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu1x1',
                  texname = '\\text{I2b12}')

I2b13 = Parameter(name = 'I2b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yu1x1',
                  texname = '\\text{I2b13}')

I2b21 = Parameter(name = 'I2b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yu2x2',
                  texname = '\\text{I2b21}')

I2b22 = Parameter(name = 'I2b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yu2x2',
                  texname = '\\text{I2b22}')

I2b23 = Parameter(name = 'I2b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yu2x2',
                  texname = '\\text{I2b23}')

I2b31 = Parameter(name = 'I2b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yu3x3',
                  texname = '\\text{I2b31}')

I2b32 = Parameter(name = 'I2b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yu3x3',
                  texname = '\\text{I2b32}')

I2b33 = Parameter(name = 'I2b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yu3x3',
                  texname = '\\text{I2b33}')

I20b11 = Parameter(name = 'I20b11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*yu1x1*complexconjugate(CKMp1x1) + CKM2x1*yu2x2*complexconjugate(CKMp2x1) + CKM3x1*yu3x3*complexconjugate(CKMp3x1)',
                   texname = '\\text{I20b11}')

I20b12 = Parameter(name = 'I20b12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*yu1x1*complexconjugate(CKMp1x1) + CKM2x2*yu2x2*complexconjugate(CKMp2x1) + CKM3x2*yu3x3*complexconjugate(CKMp3x1)',
                   texname = '\\text{I20b12}')

I20b13 = Parameter(name = 'I20b13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*yu1x1*complexconjugate(CKMp1x1) + CKM2x3*yu2x2*complexconjugate(CKMp2x1) + CKM3x3*yu3x3*complexconjugate(CKMp3x1)',
                   texname = '\\text{I20b13}')

I20b21 = Parameter(name = 'I20b21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*yu1x1*complexconjugate(CKMp1x2) + CKM2x1*yu2x2*complexconjugate(CKMp2x2) + CKM3x1*yu3x3*complexconjugate(CKMp3x2)',
                   texname = '\\text{I20b21}')

I20b22 = Parameter(name = 'I20b22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*yu1x1*complexconjugate(CKMp1x2) + CKM2x2*yu2x2*complexconjugate(CKMp2x2) + CKM3x2*yu3x3*complexconjugate(CKMp3x2)',
                   texname = '\\text{I20b22}')

I20b23 = Parameter(name = 'I20b23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*yu1x1*complexconjugate(CKMp1x2) + CKM2x3*yu2x2*complexconjugate(CKMp2x2) + CKM3x3*yu3x3*complexconjugate(CKMp3x2)',
                   texname = '\\text{I20b23}')

I20b31 = Parameter(name = 'I20b31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x1*yu1x1*complexconjugate(CKMp1x3) + CKM2x1*yu2x2*complexconjugate(CKMp2x3) + CKM3x1*yu3x3*complexconjugate(CKMp3x3)',
                   texname = '\\text{I20b31}')

I20b32 = Parameter(name = 'I20b32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x2*yu1x1*complexconjugate(CKMp1x3) + CKM2x2*yu2x2*complexconjugate(CKMp2x3) + CKM3x2*yu3x3*complexconjugate(CKMp3x3)',
                   texname = '\\text{I20b32}')

I20b33 = Parameter(name = 'I20b33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKM1x3*yu1x1*complexconjugate(CKMp1x3) + CKM2x3*yu2x2*complexconjugate(CKMp2x3) + CKM3x3*yu3x3*complexconjugate(CKMp3x3)',
                   texname = '\\text{I20b33}')

I3b11 = Parameter(name = 'I3b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp1x1*ydp1x1',
                  texname = '\\text{I3b11}')

I3b12 = Parameter(name = 'I3b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp1x2*ydp2x2',
                  texname = '\\text{I3b12}')

I3b13 = Parameter(name = 'I3b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp1x3*ydp3x3',
                  texname = '\\text{I3b13}')

I3b21 = Parameter(name = 'I3b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp2x1*ydp1x1',
                  texname = '\\text{I3b21}')

I3b22 = Parameter(name = 'I3b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp2x2*ydp2x2',
                  texname = '\\text{I3b22}')

I3b23 = Parameter(name = 'I3b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp2x3*ydp3x3',
                  texname = '\\text{I3b23}')

I3b31 = Parameter(name = 'I3b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp3x1*ydp1x1',
                  texname = '\\text{I3b31}')

I3b32 = Parameter(name = 'I3b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp3x2*ydp2x2',
                  texname = '\\text{I3b32}')

I3b33 = Parameter(name = 'I3b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp3x3*ydp3x3',
                  texname = '\\text{I3b33}')

I4b11 = Parameter(name = 'I4b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp1x1*yu1x1',
                  texname = '\\text{I4b11}')

I4b12 = Parameter(name = 'I4b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp1x2*yu1x1',
                  texname = '\\text{I4b12}')

I4b13 = Parameter(name = 'I4b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp1x3*yu1x1',
                  texname = '\\text{I4b13}')

I4b21 = Parameter(name = 'I4b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp2x1*yu2x2',
                  texname = '\\text{I4b21}')

I4b22 = Parameter(name = 'I4b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp2x2*yu2x2',
                  texname = '\\text{I4b22}')

I4b23 = Parameter(name = 'I4b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp2x3*yu2x2',
                  texname = '\\text{I4b23}')

I4b31 = Parameter(name = 'I4b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp3x1*yu3x3',
                  texname = '\\text{I4b31}')

I4b32 = Parameter(name = 'I4b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp3x2*yu3x3',
                  texname = '\\text{I4b32}')

I4b33 = Parameter(name = 'I4b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKMp3x3*yu3x3',
                  texname = '\\text{I4b33}')

I5b11 = Parameter(name = 'I5b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x1*ye1x1*complexconjugate(PMNS1x1) + PMNSp2x1*ye2x2*complexconjugate(PMNS2x1) + PMNSp3x1*ye3x3*complexconjugate(PMNS3x1)',
                  texname = '\\text{I5b11}')

I5b12 = Parameter(name = 'I5b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x2*ye1x1*complexconjugate(PMNS1x1) + PMNSp2x2*ye2x2*complexconjugate(PMNS2x1) + PMNSp3x2*ye3x3*complexconjugate(PMNS3x1)',
                  texname = '\\text{I5b12}')

I5b13 = Parameter(name = 'I5b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x3*ye1x1*complexconjugate(PMNS1x1) + PMNSp2x3*ye2x2*complexconjugate(PMNS2x1) + PMNSp3x3*ye3x3*complexconjugate(PMNS3x1)',
                  texname = '\\text{I5b13}')

I5b21 = Parameter(name = 'I5b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x1*ye1x1*complexconjugate(PMNS1x2) + PMNSp2x1*ye2x2*complexconjugate(PMNS2x2) + PMNSp3x1*ye3x3*complexconjugate(PMNS3x2)',
                  texname = '\\text{I5b21}')

I5b22 = Parameter(name = 'I5b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x2*ye1x1*complexconjugate(PMNS1x2) + PMNSp2x2*ye2x2*complexconjugate(PMNS2x2) + PMNSp3x2*ye3x3*complexconjugate(PMNS3x2)',
                  texname = '\\text{I5b22}')

I5b23 = Parameter(name = 'I5b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x3*ye1x1*complexconjugate(PMNS1x2) + PMNSp2x3*ye2x2*complexconjugate(PMNS2x2) + PMNSp3x3*ye3x3*complexconjugate(PMNS3x2)',
                  texname = '\\text{I5b23}')

I5b31 = Parameter(name = 'I5b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x1*ye1x1*complexconjugate(PMNS1x3) + PMNSp2x1*ye2x2*complexconjugate(PMNS2x3) + PMNSp3x1*ye3x3*complexconjugate(PMNS3x3)',
                  texname = '\\text{I5b31}')

I5b32 = Parameter(name = 'I5b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x2*ye1x1*complexconjugate(PMNS1x3) + PMNSp2x2*ye2x2*complexconjugate(PMNS2x3) + PMNSp3x2*ye3x3*complexconjugate(PMNS3x3)',
                  texname = '\\text{I5b32}')

I5b33 = Parameter(name = 'I5b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x3*ye1x1*complexconjugate(PMNS1x3) + PMNSp2x3*ye2x2*complexconjugate(PMNS2x3) + PMNSp3x3*ye3x3*complexconjugate(PMNS3x3)',
                  texname = '\\text{I5b33}')

I6b11 = Parameter(name = 'I6b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye1x1*complexconjugate(PMNS1x1)',
                  texname = '\\text{I6b11}')

I6b12 = Parameter(name = 'I6b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye2x2*complexconjugate(PMNS2x1)',
                  texname = '\\text{I6b12}')

I6b13 = Parameter(name = 'I6b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye3x3*complexconjugate(PMNS3x1)',
                  texname = '\\text{I6b13}')

I6b21 = Parameter(name = 'I6b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye1x1*complexconjugate(PMNS1x2)',
                  texname = '\\text{I6b21}')

I6b22 = Parameter(name = 'I6b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye2x2*complexconjugate(PMNS2x2)',
                  texname = '\\text{I6b22}')

I6b23 = Parameter(name = 'I6b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye3x3*complexconjugate(PMNS3x2)',
                  texname = '\\text{I6b23}')

I6b31 = Parameter(name = 'I6b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye1x1*complexconjugate(PMNS1x3)',
                  texname = '\\text{I6b31}')

I6b32 = Parameter(name = 'I6b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye2x2*complexconjugate(PMNS2x3)',
                  texname = '\\text{I6b32}')

I6b33 = Parameter(name = 'I6b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ye3x3*complexconjugate(PMNS3x3)',
                  texname = '\\text{I6b33}')

I7b11 = Parameter(name = 'I7b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu1x1*complexconjugate(PMNS1x1)',
                  texname = '\\text{I7b11}')

I7b12 = Parameter(name = 'I7b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu1x1*complexconjugate(PMNS2x1)',
                  texname = '\\text{I7b12}')

I7b13 = Parameter(name = 'I7b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu1x1*complexconjugate(PMNS3x1)',
                  texname = '\\text{I7b13}')

I7b21 = Parameter(name = 'I7b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu2x2*complexconjugate(PMNS1x2)',
                  texname = '\\text{I7b21}')

I7b22 = Parameter(name = 'I7b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu2x2*complexconjugate(PMNS2x2)',
                  texname = '\\text{I7b22}')

I7b23 = Parameter(name = 'I7b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu2x2*complexconjugate(PMNS3x2)',
                  texname = '\\text{I7b23}')

I7b31 = Parameter(name = 'I7b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu3x3*complexconjugate(PMNS1x3)',
                  texname = '\\text{I7b31}')

I7b32 = Parameter(name = 'I7b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu3x3*complexconjugate(PMNS2x3)',
                  texname = '\\text{I7b32}')

I7b33 = Parameter(name = 'I7b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ynu3x3*complexconjugate(PMNS3x3)',
                  texname = '\\text{I7b33}')

I8b11 = Parameter(name = 'I8b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x1*ye1x1',
                  texname = '\\text{I8b11}')

I8b12 = Parameter(name = 'I8b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x2*ye1x1',
                  texname = '\\text{I8b12}')

I8b13 = Parameter(name = 'I8b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x3*ye1x1',
                  texname = '\\text{I8b13}')

I8b21 = Parameter(name = 'I8b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp2x1*ye2x2',
                  texname = '\\text{I8b21}')

I8b22 = Parameter(name = 'I8b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp2x2*ye2x2',
                  texname = '\\text{I8b22}')

I8b23 = Parameter(name = 'I8b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp2x3*ye2x2',
                  texname = '\\text{I8b23}')

I8b31 = Parameter(name = 'I8b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp3x1*ye3x3',
                  texname = '\\text{I8b31}')

I8b32 = Parameter(name = 'I8b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp3x2*ye3x3',
                  texname = '\\text{I8b32}')

I8b33 = Parameter(name = 'I8b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp3x3*ye3x3',
                  texname = '\\text{I8b33}')

I9b11 = Parameter(name = 'I9b11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x1*yn1x1',
                  texname = '\\text{I9b11}')

I9b12 = Parameter(name = 'I9b12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x2*yn2x2',
                  texname = '\\text{I9b12}')

I9b13 = Parameter(name = 'I9b13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp1x3*yn3x3',
                  texname = '\\text{I9b13}')

I9b21 = Parameter(name = 'I9b21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp2x1*yn1x1',
                  texname = '\\text{I9b21}')

I9b22 = Parameter(name = 'I9b22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp2x2*yn2x2',
                  texname = '\\text{I9b22}')

I9b23 = Parameter(name = 'I9b23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp2x3*yn3x3',
                  texname = '\\text{I9b23}')

I9b31 = Parameter(name = 'I9b31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp3x1*yn1x1',
                  texname = '\\text{I9b31}')

I9b32 = Parameter(name = 'I9b32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp3x2*yn2x2',
                  texname = '\\text{I9b32}')

I9b33 = Parameter(name = 'I9b33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNSp3x3*yn3x3',
                  texname = '\\text{I9b33}')

