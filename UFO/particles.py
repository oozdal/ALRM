# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Fri 21 Jun 2019 18:24:06


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

A = Particle(pdg_code = 22,
             name = 'A',
             antiname = 'A',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'A',
             antitexname = 'A',
             charge = 0,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

Zp = Particle(pdg_code = 32,
              name = 'Zp',
              antiname = 'Zp',
              spin = 3,
              color = 1,
              mass = Param.MZp,
              width = Param.WZp,
              texname = 'Zp',
              antitexname = 'Zp',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

W = Particle(pdg_code = 24,
             name = 'W',
             antiname = 'W~',
             spin = 3,
             color = 1,
             mass = Param.MW,
             width = Param.WW,
             texname = 'W',
             antitexname = 'W~',
             charge = 1,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

W__tilde__ = W.anti()

Wp = Particle(pdg_code = 34,
              name = 'Wp',
              antiname = 'Wp~',
              spin = 3,
              color = 1,
              mass = Param.MWp,
              width = Param.WWp,
              texname = 'Wp',
              antitexname = 'Wp~',
              charge = 1,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

Wp__tilde__ = Wp.anti()

G = Particle(pdg_code = 21,
             name = 'G',
             antiname = 'G',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'G',
             antitexname = 'G',
             charge = 0,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

ghG = Particle(pdg_code = 9000001,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LNumber = 0,
               YBL = 0)

ghG__tilde__ = ghG.anti()

H0 = Particle(pdg_code = 25,
              name = 'H0',
              antiname = 'H0',
              spin = 1,
              color = 1,
              mass = Param.MH0,
              width = Param.WH0,
              texname = 'H0',
              antitexname = 'H0',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

H1 = Particle(pdg_code = 35,
              name = 'H1',
              antiname = 'H1',
              spin = 1,
              color = 1,
              mass = Param.MH1,
              width = Param.WH1,
              texname = 'H1',
              antitexname = 'H1',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

H2 = Particle(pdg_code = 45,
              name = 'H2',
              antiname = 'H2',
              spin = 1,
              color = 1,
              mass = Param.MH2,
              width = Param.WH2,
              texname = 'H2',
              antitexname = 'H2',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

H3 = Particle(pdg_code = 55,
              name = 'H3',
              antiname = 'H3',
              spin = 1,
              color = 1,
              mass = Param.MH3,
              width = Param.WH3,
              texname = 'H3',
              antitexname = 'H3',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

A1 = Particle(pdg_code = 36,
              name = 'A1',
              antiname = 'A1',
              spin = 1,
              color = 1,
              mass = Param.MA1,
              width = Param.WA1,
              texname = 'A1',
              antitexname = 'A1',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

A2 = Particle(pdg_code = 46,
              name = 'A2',
              antiname = 'A2',
              spin = 1,
              color = 1,
              mass = Param.MA2,
              width = Param.WA2,
              texname = 'A2',
              antitexname = 'A2',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

Hp1 = Particle(pdg_code = 37,
               name = 'Hp1',
               antiname = 'Hp1~',
               spin = 1,
               color = 1,
               mass = Param.MHp1,
               width = Param.WHp1,
               texname = 'Hp1',
               antitexname = 'Hp1~',
               charge = 1,
               GhostNumber = 0,
               LNumber = 0,
               YBL = 0)

Hp1__tilde__ = Hp1.anti()

Hp2 = Particle(pdg_code = 47,
               name = 'Hp2',
               antiname = 'Hp2~',
               spin = 1,
               color = 1,
               mass = Param.MHp2,
               width = Param.WHp2,
               texname = 'Hp2',
               antitexname = 'Hp2~',
               charge = 1,
               GhostNumber = 0,
               LNumber = 0,
               YBL = 0)

Hp2__tilde__ = Hp2.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.Mve,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.Mvm,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.Mvt,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LNumber = 0,
                      YBL = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LNumber = 0,
                       YBL = 0)

mu__plus__ = mu__minus__.anti()

tau__minus__ = Particle(pdg_code = 15,
                        name = 'tau-',
                        antiname = 'tau+',
                        spin = 2,
                        color = 1,
                        mass = Param.MTA,
                        width = Param.ZERO,
                        texname = 'tau-',
                        antitexname = 'tau+',
                        charge = -1,
                        GhostNumber = 0,
                        LNumber = 0,
                        YBL = 0)

tau__plus__ = tau__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LNumber = 0,
             YBL = 0)

b__tilde__ = b.anti()

P__tilde__ne = Particle(pdg_code = 18,
                        name = '~ne',
                        antiname = '~ne~',
                        spin = 2,
                        color = 1,
                        mass = Param.Mne,
                        width = Param.ZERO,
                        texname = '~ne',
                        antitexname = '~ne~',
                        charge = 0,
                        GhostNumber = 0,
                        LNumber = 0,
                        YBL = 0)

P__tilde__ne__tilde__ = P__tilde__ne.anti()

P__tilde__nm = Particle(pdg_code = 6000014,
                        name = '~nm',
                        antiname = '~nm~',
                        spin = 2,
                        color = 1,
                        mass = Param.Mnm,
                        width = Param.Wnm,
                        texname = '~nm',
                        antitexname = '~nm~',
                        charge = 0,
                        GhostNumber = 0,
                        LNumber = 0,
                        YBL = 0)

P__tilde__nm__tilde__ = P__tilde__nm.anti()

P__tilde__nt = Particle(pdg_code = 6000016,
                        name = '~nt',
                        antiname = '~nt~',
                        spin = 2,
                        color = 1,
                        mass = Param.Mnt,
                        width = Param.Wnt,
                        texname = '~nt',
                        antitexname = '~nt~',
                        charge = 0,
                        GhostNumber = 0,
                        LNumber = 0,
                        YBL = 0)

P__tilde__nt__tilde__ = P__tilde__nt.anti()

dp = Particle(pdg_code = 6000001,
              name = 'dp',
              antiname = 'dp~',
              spin = 2,
              color = 3,
              mass = Param.MDP,
              width = Param.ZERO,
              texname = 'dp',
              antitexname = 'dp~',
              charge = -1/3,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

dp__tilde__ = dp.anti()

sp = Particle(pdg_code = 6000003,
              name = 'sp',
              antiname = 'sp~',
              spin = 2,
              color = 3,
              mass = Param.MSP,
              width = Param.WSP,
              texname = 'sp',
              antitexname = 'sp~',
              charge = -1/3,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

sp__tilde__ = sp.anti()

bp = Particle(pdg_code = 6000005,
              name = 'bp',
              antiname = 'bp~',
              spin = 2,
              color = 3,
              mass = Param.MBP,
              width = Param.WBP,
              texname = 'bp',
              antitexname = 'bp~',
              charge = -1/3,
              GhostNumber = 0,
              LNumber = 0,
              YBL = 0)

bp__tilde__ = bp.anti()

