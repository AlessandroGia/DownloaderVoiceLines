
def Vgs(url):


	#print(url) ###DEBUG
	
	urlO = url
	url = url.lower()

	SELECT = "select"
	INTRO = "intro"
	PASSIVE = "passive"
	ABILITY1 = "ability_1"
	ABILITY2 = "ability_2"
	ABILITY3 = "ability_3"
	ABILITY4 = "ability_4"
	MOVEMENT = "movement"
	HEALTH_LOW = "health_low"
	WARD_PLACED = "ward_placed"
	PURCHASE_CONSUMABLE = "purchase_consumable"
	PURCHASE_RECOMMENDED = "purchase_recommended"
	PURCHASE_NOTRECOMMENDED = "purchase_notrecommended"
	KILL_STREAK = "kill_streak"
	KILL_JUNGLEBOSS = "kill_jungleboss"
	KILL_TOWER = "kill_tower"
	DEATH = "death"
	VET = "vet"
	TAUNT_DIRECTED = "taunt_directed" #TAUNT e DIRECT TAUNT vanno in conflitto
	SPECIAL = "special"
	VEJ = "vej"
	VEL = "vel"

	VA1 = "va1"
	VA2 = "va2"
	VA3 = "va3"
	VAA = "vaa"
	VAF = "vaf"
	VAG = "vag"
	VAM = "vam"
	VAN = "van"

	VAT1 = "vat1"
	VAT2 = "vat2"
	VAT3 = "vat3"

	#VBJ = "vbj"
	VB1 = "vb1"
	VB2 = "vb2"
	VB3 = "vb3"

	VBA = "vba"
	VBB = "vbb"
	VBD = "vbd"
	VBE = "vbe"
	VBF = "vbf"
	VBG = "vbg"
	VBM = "vbm"
	VBS = "vbs"

	VBJ1 = "vbj1"
	VBJ2 = "vbj2"
	VBJ3 = "vbj3"
	VBJJ = "vbjj"

	VC1 = "vc1"
	VC2 = "vc2"
	VC3 = "vc3"
	VCB = "vcb"
	VCC = "vcc"
	VCJ = "vcj"

	VD1 = "vd1"
	VD2 = "vd2"
	VD3 = "vd3"
	VDD = "vdd"
	VDF = "vdf"
	VDG = "vdg"
	VDT = "vdt"
	VDM = "vdm"

	VEA = "vea"
	VEG = "veg"
	VER = "ver"
	VEW = "vew"

	VF1 = "vf1"
	VF2 = "vf2"
	VF3 = "vf3"
	VFF = "vff"

	VG1 = "vg1"
	VG2 = "vg2"
	VG3 = "vg3"
	VGG = "vgg"

	VH1 = "vh1"
	VH2 = "vh2"
	VH3 = "vh3"
	VHH = "vhh"
	VHS = "vhs"

	VI1 = "vi1"
	VI2 = "vi2"
	VI3 = "vi3"
	VII = "vii"

	VQ1 = "vq1"
	VQ2 = "vq2"
	VQ3 = "vq3"
	VQF = "vqf"
	VQG = "vqg"
	VQN = "vqn"
	VQQ = "vqq"

	VR1 = "vr1"
	VR2 = "vr2"
	VR3 = "vr3"
	VRJ = "vrj"
	VRR = "vrr"
	VRS = "vrs"

	VSO = "vso"
	VSR = "vsr"
	VSS = "vss"

	VSA1 = "vsa1"
	VSA2 = "vsa2"
	VSA3 = "vsa3"
	VSAA = "vsaa"
	VSAF = "vsaf"
	VSAG = "vsag"
	VSAM = "vsam"

	VSBB = "vsbb"
	VSBN = "vsbn"
	VSBT = "vsbt"

	VSD1 = 'vsd1'
	VSD2 = 'vsd2'
	VSD3 = 'vsd3'
	VSDD = 'vsdd'
	VSDF = 'vsdf'
	VSDG = 'vsdg'
	VSDM = 'vsdm'

	VSG1 = "vsg1"
	VSG2 = "vsg2"
	VSG3 = "vsg3"
	VSGG = "vsgg"

	VSQ1 = "vsq1"
	VSQ2 = "vsq2"
	VSQ3 = "vsq3"
	VSQQ = "vsqq"

	VST1 = "vst1"
	VST2 = "vst2"
	VST3 = "vst3"
	VSTB = "vstb"
	VSTT = "vstt"


	VT1 = "vt1"
	VT2 = "vt2"
	VT3 = "vt3"
	VTT = "vtt"

	VVA = "vva"
	VVB = "vvb"
	VVC = "vvc"
	VVK = "vvk"
	VVM = "vvm"
	VVN = "vvn"
	VVP = "vvp"
	VVS = "vvs"
	VVT = "vvt"
	VVW = "vvw"
	VVX = "vvx"
	VVY = "vvy"

	VVGB = "vvgb"
	VVGF = "vvgf"
	VVGG = "vvgg"
	VVGH = "vvgh"
	VVGL = "vvgl"
	VVGN = "vvgn"
	VVGO = "vvgo"
	VVGQ = "vvgq"
	VVGR = "vvgr"
	VVGS = "vvgs"
	VVGT = "vvgt"
	VVGW = "vvgw"

	VVVA = "vvva"
	VVVB = "vvvb"
	VVVC = "vvvc"
	VVVD = "vvvd"
	VVVE = "vvve"
	VVVF = "vvvf"
	VVVG = "vvvg"
	VVVJ = "vvvj"
	VVVP = "vvvp"
	VVVR = "vvvr"
	VVVS = "vvvs"
	VVVT = "vvvt"
	VVVW = "vvvw"
	VVVX = "vvvx"

	
	if SELECT.lower() in url:
		return SELECT 
	
	if INTRO.lower() in url:
		return INTRO 
	
	if PASSIVE.lower() in url:
		return PASSIVE 

	if ABILITY1.lower() in url:
		return ABILITY1 
	if "Ability1" in urlO:
		return ABILITY1 
	 
	if ABILITY2.lower() in url:
		return ABILITY2
	if "Ability2" in urlO:
		return ABILITY2
	if "Grunt_e".lower() in url:
		return ABILITY2

	if ABILITY3.lower() in url:
		return ABILITY3
	if "Ability3" in urlO:
		return ABILITY3 

	if ABILITY4.lower() in url:
		return ABILITY4
	if "Ability4" in urlO:
		return ABILITY4 
	if "Grunt_p".lower() in url:
		return ABILITY4
	if "Grunt_r".lower() in url:
		return ABILITY4 

	if "move".lower() in url:
		return MOVEMENT
	
	if HEALTH_LOW.lower() in url:
		return HEALTH_LOW 
	
	if WARD_PLACED.lower() in url:
		return WARD_PLACED 
	
	if PURCHASE_CONSUMABLE.lower() in url:
		return PURCHASE_CONSUMABLE 
	
	if PURCHASE_RECOMMENDED.lower() in url:
		return PURCHASE_RECOMMENDED 
	
	if PURCHASE_NOTRECOMMENDED.lower() in url:
		return PURCHASE_NOTRECOMMENDED 
	
	if KILL_STREAK.lower() in url:
		return KILL_STREAK 
	
	if KILL_JUNGLEBOSS.lower() in url:
		return KILL_JUNGLEBOSS 
	
	if KILL_TOWER.lower() in url:
		return KILL_TOWER 
	
	if DEATH.lower() in url:
		return DEATH 

	if "Self_Attack_1".lower() in url: # urlO.lower()
		return VSA1
	if "VSA1".lower() in url:
		return VSA1 

	if "Self_Attack_2".lower() in url: #
		return VSA2
	if "VSA2".lower() in url:
		return VSA2 
	
	if "Self_Attack_3".lower() in url: #
		return VSA3
	if "VSA3".lower() in url:
		return VSA3 
	
	if "Self_Attack_F".lower() in url: #
		return VSAF
	if "VSAF".lower() in url:
		return VSAF
	
	if "Self_Attack_G".lower() in url: #
		return VSAG
	if "VSAG".lower() in url:
		return VSAG
	
	if "Self_Attack_M".lower() in url: #
		return VSAM
	if "Self_Attack_T".lower() in url: #
		return VSAM
	if "VSAM".lower() in url:
		return VSAM 

	if "Self_Attack".lower() in url: #
		return VSAA
	if "VSAA".lower() in url:
		return VSAA 
	
	if "self_b".lower() in url:
		return VSBB
	if "VSBB".lower() in url:
		return VSBB 
	
	if "jungle_buff_n".lower() in url:
		return VSBN
	if "VSBN".lower() in url:
		return VSBN 
	
	if "jungle_buff_c".lower() in url:
		return VSBT
	if "VSBT".lower() in url:
		return VSBT 
	
	if "self_defend_1".lower() in url:
		return VSD1
	if "VSD1".lower() in url:
		return VSD1 
	
	if "self_defend_2".lower() in url:
		return VSD2
	if "VSD2".lower() in url:
		return VSD2 
	 
	if "self_defend_3".lower() in url:
		return VSD3
	if "VSD3".lower() in url:
		return VSD3
	
	if "self_defend_f".lower() in url:
		return VSDF
	if "VSDF".lower() in url:
		return VSDF 
	
	if "self_defend_g".lower() in url:
		return VSDG
	if "VSDG".lower() in url:
		return VSDG 
	
	if "self_defend_m".lower() in url:
		return VSDM
	if "self_defend_t".lower() in url:
		return VSDM
	if "VSDM".lower() in url:
		return VSDM 

	if "self_defend".lower() in url:
		return VSDD
	if "VSDD".lower() in url:
		return VSDD
	
	if "self_gank_1".lower() in url:
		return VSG1
	if "VSG1".lower() in url:
		return VSG1 
	
	if "self_gank_2".lower() in url:
		return VSG2
	if "VSG2".lower() in url:
		return VSG2
	
	if "self_gank_3".lower() in url:
		return VSG3
	if "VSG3".lower() in url:
		return VSG3
	
	if "self_gank".lower() in url:
		return VSGG
	if "VSGG".lower() in url:
		return VSGG
	
	if "self_ward_1".lower() in url:
		return VSQ1
	if "VSQ1".lower() in url:
		return VSQ1
	
	if "self_ward_2".lower() in url:
		return VSQ2
	if "VSQ2".lower() in url:
		return VSQ2 
	
	if "self_ward_3".lower() in url:
		return VSQ3
	if "VSQ3".lower() in url:
		return VSQ3 
	
	if "self_ward".lower() in url:
		return VSQQ
	if "VSQQ".lower() in url:
		return VSQQ 
	
	if "self_returned_1".lower() in url:
		return VST1
	if "VST1".lower() in url:
		return VST1
	
	if "self_returned_2".lower() in url:
		return VST2
	if "VST2".lower() in url:
		return VST2 
	
	if "self_returned_3".lower() in url:
		return VST3
	if "VST3".lower() in url:
		return VST3

	if "VSTB".lower() in url:
		return VSTB
	
	if "self_returned_e".lower() in url:
		return VSTT
	if "VSTT".lower() in url:
		return VSTT
		
	if TAUNT_DIRECTED.lower() in url:
		return 'vetd'

	if "taunt".lower() in url:
		return VET  
	
	if "joke".lower() in url:
		return VEJ 
	
	if "laugh".lower() in url:
		return VEL 

	if "special".lower() in url:
		return SPECIAL
	
	if "attack_1".lower() in url:
		return VA1 
	if "VA1" in urlO:
		return VA1
	
	if "attack_2".lower() in url:
		return VA2
	if "VA2" in urlO:
		return VA2
	
	if "attack_3".lower() in url:
		return VA3 
	if "VA3" in urlO:
		return VA3
	
	if "attack_a".lower() in url:
		return VAA 
	if "VAA" in urlO:
		return VAA
	
	if "attack_f".lower() in url:
		return VAF
	if "VAF" in urlO:
		return VAF

	if "attack_g".lower() in url:
		return VAG
	if "VAG" in urlO:
		return VAG
	
	if "attack_t".lower() in url:
		return VAM 
	if "attack_m".lower() in url:
		return VAM
	if "VAM" in urlO:
		return VAM
	
	if "arena_m".lower() in url:
		return VAN 
	if "VAN" in urlO:
		return VAN
	
	if "tower_1".lower() in url:
		return VAT1 
	if "phoenix_1".lower() in url:
		return VAT1
	if "VAT1" in urlO:
		return VAT1
	
	if "tower_2".lower() in url:
		return VAT2 
	if "phoenix_2".lower() in url:
		return VAT2 
	if "VAT2" in urlO:
		return VAT2

	if "tower_3".lower() in url:
		return VAT3 
	if "phoenix_3".lower() in url:
		return VAT3
	if "VAT3" in urlO:
		return VAT3

	if "enemy_1".lower() in url:
		return VB1
	if "VB1".lower() in url:
		return VB1
	
	if "enemy_2".lower() in url:
		return VB2
	if "VB2".lower() in url:
		return VB2
	
	if "enemy_3".lower() in url:
		return VB3
	if "VB3".lower() in url:
		return VB3
	
	if "ultimate_enemy_a".lower() in url:
		return VBA
	if "VBA".lower() in url:
		return VBA 
	
	if "enemy_b".lower() in url:
		return VBB
	if "VBB".lower() in url:
		return VBB
	
	if "ultimate_enemy_d".lower() in url:
		return VBD
	if "VBD".lower() in url:
		return VBD 
	
	if "enemy_e".lower() in url:
		return VBE
	if "VBE".lower() in url:
		return VBE
	
	if "enemy_f".lower() in url:
		return VBF
	if "VBF".lower() in url:
		return VBF 
	
	if "enemy_g".lower() in url:
		return VBG
	if "VBG".lower() in url:
		return VBG
	
	if "enemy_t".lower() in url:
		return VBM
	if "enemy_m".lower() in url: ##
		return VBM ##
	if "VBM".lower() in url:
		return VBM 
	
	if "enemy_s".lower() in url:
		return VBS
	if "VBS".lower() in url:
		return VBS
	
	if "enemy_jungle_1".lower() in url:
		return VBJ1
	if "VBJ1".lower() in url:
		return VBJ1
	
	if "enemy_jungle_2".lower() in url:
		return VBJ2 
	if "VBJ2".lower() in url:
		return VBJ2

	if "VBJ3".lower() in url:
		return VBJ3

	if "enemy_j".lower() in url:
		return VBJJ
	if "VBJJ".lower() in url:
		return VBJJ
	
	if "careful_1".lower() in url:
		return VC1
	if "VC1".lower() in url:
		return VC1
	
	if "careful_2".lower() in url:
		return VC2 
	if "VC2".lower() in url:
		return VC2

	if "careful_3".lower() in url:
		return VC3
	if "VC3".lower() in url:
		return VC3
	
	if "careful_b".lower() in url:
		return VCB
	if "VCB".lower() in url:
		return VCB
	
	if "careful_c".lower() in url:
		return VCC
	if "VCC".lower() in url:
		return VCC
	
	if "careful_j".lower() in url:
		return VCJ
	if "VCJ".lower() in url:
		return VCJ 
	 
	if "defend_1".lower() in url:
		return VD1
	if "VD1".lower() in url:
		return VD1
	
	if "defend_2".lower() in url:
		return VD2
	if "VD2".lower() in url:
		return VD2
	
	if "defend_3".lower() in url:
		return VD3
	if "VD3".lower() in url:
		return VD3
	
	if "defend_d".lower() in url:
		return VDD
	if "VDD".lower() in url:
		return VDD 
	
	if "defend_f".lower() in url:
		return VDF
	if "VDF".lower() in url:
		return VDF 
	
	if "defend_g".lower() in url:
		return VDG
	if "VDG".lower() in url:
		return VDG
	
	if "defend_t".lower() in url:
		return VDT
	if "VDT".lower() in url:
		return VDT
	
	if "arena_p".lower() in url:
		return VDM
	if "defend_m".lower() in url: ###
		return VDM ###
	if "VDM".lower() in url:
		return VDM
	
	if "emote_a".lower() in url:
		return VEA
	if "VEA".lower() in url:
		return VEA
	
	if "emote_g".lower() in url:
		return VEG
	if "VEG".lower() in url:
		return VEG
	
	if "emote_r".lower() in url:
		return VER
	if "VER".lower() in url:
		return VER 
	
	if "emote_w".lower() in url:
		return VEW
	if "VEW".lower() in url:
		return VEW
	
	if "mia_1".lower() in url:
		return VF1
	if "VF1".lower() in url:
		return VF1 
	 
	if "mia_2".lower() in url:
		return VF2
	if "VF2".lower() in url:
		return VF2 
	
	if "mia_3".lower() in url:
		return VF3
	if "VF3".lower() in url:
		return VF3  
	
	if "mia_m".lower() in url:
		return VFF
	if "VFF".lower() in url:
		return VFF
	
	if "gank_1".lower() in url:
		return VG1
	if "VG1".lower() in url:
		return VG1 
	
	if "gank_2".lower() in url:
		return VG2
	if "VG2".lower() in url:
		return VG2 
	 
	if "gank_3".lower() in url:
		return VG3
	if "VG3".lower() in url:
		return VG3
	
	if "gank_g".lower() in url:
		return VGG
	if "VGG".lower() in url:
		return VGG 
	
	if "help_1".lower() in url:
		return VH1
	if "VH1".lower() in url:
		return VH1 
	
	if "help_2".lower() in url:
		return VH2
	if "VH2".lower() in url:
		return VH2  
	 
	if "help_3".lower() in url:
		return VH3
	if "VH3".lower() in url:
		return VH3 
	
	if "help".lower() in url:
		return VHH
	if "VHH".lower() in url:
		return VHH  
	
	if "help_s".lower() in url:
		return VHS
	if "VHS".lower() in url:
		return VHS 
	
	if "incoming_1".lower() in url:
		return VI1
	if "VI1".lower() in url:
		return VI1  
	
	if "incoming_2".lower() in url:
		return VI2
	if "VI2".lower() in url:
		return VI2 
	
	if "incoming_3".lower() in url:
		return VI3
	if "VI3".lower() in url:
		return VI3
	 
	if "incoming_i".lower() in url:
		return VII
	if "VII".lower() in url:
		return VII
	
	if "ward_1".lower() in url:
		return VQ1
	if "Q1".lower() in url:
		return VQ1 
	
	if "ward_2".lower() in url:
		return VQ2
	if "Q2".lower() in url:
		return VQ2 
	
	if "ward_3".lower() in url:
		return VQ3
	if "Q3".lower() in url:
		return VQ3 
	
	if "ward_f".lower() in url:
		return VQF
	if "QF".lower() in url:
		return VQF
	
	if "ward_g".lower() in url:
		return VQG
	if "QG".lower() in url:
		return VQG
	 
	if "ward_n".lower() in url:
		return VQN
	if "QN".lower() in url:
		return VQN
	
	if "ward".lower() in url:
		return VQQ 
	if "QQ".lower() in url:
		return VQQ
	
	if "retreat_1".lower() in url:
		return VR1
	if "VR1".lower() in url:
		return VR1 
	
	if "retreat_2".lower() in url:
		return VR2
	if "VR2".lower() in url:
		return VR2 
	
	if "retreat_3".lower() in url:
		return VR3
	if "VR3".lower() in url:
		return VR3 
	
	if "retreat_j".lower() in url:
		return VRJ
	if "VRJ".lower() in url:
		return VRJ 
	 
	if "retreat_r".lower() in url:
		return VRR
	if "VRR".lower() in url:
		return VRR
	 
	if "retreat_s".lower() in url:
		return VRS
	if "VRS".lower() in url:
		return VRS
	
	if "self_o".lower() in url:
		return VSO
	if "VSO".lower() in url:
		return VSO
	
	if "self_r".lower() in url:
		return VSR
	if "VSR".lower() in url:
		return VSR
	
	if "self_s".lower() in url:
		return VSS
	if "VSS".lower() in url:
		return VSS  

	if "returned_1".lower() in url:
		return VT1
	if "VT1".lower() in url:
		return VT1
	
	if "returned_2".lower() in url:
		return VT2
	if "VT2".lower() in url:
		return VT2

	if "returned_3".lower() in url:
		return VT3
	if "VT3".lower() in url:
		return VT3

	if "returned".lower() in url:
		return VTT
	if "VTT".lower() in url:
		return VTT
	
	if "VVA".lower() in url:
		return VVA 
	
	if "brb".lower() in url:
		return VVB
	if "VVB".lower() in url:
		return VVB 
	
	if "completed".lower() in url:
		return VVC
	if "VVC".lower() in url:
		return VVC  
	
	if "afk".lower() in url:
		return VVK
	if "VVK".lower() in url:
		return VVK 
	
	if "other_g_m".lower() in url:
		return VVM
	if "VVM".lower() in url:
		return VVM 
	
	if "emote_no".lower() in url:
		return VVN
	if "VVN".lower() in url:
		return VVN 
	
	if "emote_please".lower() in url:
		return VVP
	if "VVP".lower() in url:
		return VVP  
	
	if "other_s".lower() in url:
		return VVS
	if "VVS".lower() in url:
		return VVS 
	
	if "thanks".lower() in url:
		return VVT
	if "VVT".lower() in url:
		return VVT 
	
	if "other_w".lower() in url:
		return VVW
	if "VVW".lower() in url:
		return VVW  
	
	if "cancel".lower() in url:
		return VVX
	if "VVX".lower() in url:
		return VVX  
	
	if "emote_yes".lower() in url:
		return VVY
	if "VVY".lower() in url:
		return VVY  
	
	if "other_g_b".lower() in url:
		return VVGB
	if "VVGB".lower() in url:
		return VVGB  
	
	if "emote_f".lower() in url:
		return VVGF
	if "VVGF".lower() in url:
		return VVGF 
	
	if "other_g_g".lower() in url:
		return VVGG
	if "VVGG".lower() in url:
		return VVGG 
	
	if "other_g_h".lower() in url:
		return VVGH
	if "VVGH".lower() in url:
		return VVGH 
	
	if "other_g_l".lower() in url:
		return VVGL
	if "VVGL".lower() in url:
		return VVGL 
	
	if "nicejob".lower() in url:
		return VVGN
	if "VVGN".lower() in url:
		return VVGN 
	
	if "other_g_o".lower() in url:
		return VVGO
	if "VVGO".lower() in url:
		return VVGO 
	
	if "other_g_q".lower() in url:
		return VVGQ
	if "VVGQ".lower() in url:
		return VVGQ
	 
	if "other_g_r".lower() in url:
		return VVGR
	if "VVGR".lower() in url:
		return VVGR
	
	if "other_g_s".lower() in url:
		return VVGS
	if "VVGS".lower() in url:
		return VVGS 
	
	if "other_g_t".lower() in url:
		return VVGT
	if "VVGT".lower() in url:
		return VVGT 
	
	if "other_g_w".lower() in url:
		return VVGW 
	if "VVGW".lower() in url:
		return VVGW
	
	if "other_v_a".lower() in url:
		return VVVA
	if "VVVA".lower() in url:
		return VVVA 
	
	if "other_v_b".lower() in url:
		return VVVB
	if "VVVB".lower() in url:
		return VVVB 
	 
	if "other_v_c".lower() in url:
		return VVVC
	if "VVVC".lower() in url:
		return VVVC
	
	if "other_v_d".lower() in url:
		return VVVD
	if "VVVD".lower() in url:
		return VVVD
	 
	if "other_v_w".lower() in url: #####
		return VVVE
	if "VVVE".lower() in url:
		return VVVE
	 
	if "other_v_f".lower() in url:
		return VVVF
	if "VVVF".lower() in url:
		return VVVF
	
	if "other_v_g".lower() in url:
		return VVVG
	if "VVVG".lower() in url:
		return VVVG
	
	if "other_v_j".lower() in url:
		return VVVJ
	if "VVVJ".lower() in url:
		return VVVJ 
	
	if "other_v_p".lower() in url:
		return VVVP
	if "VVVP".lower() in url:
		return VVVP 
	
	if "other_v_r".lower() in url:
		return VVVR
	if "VVVR".lower() in url:
		return VVVR 
	
	if "other_v_s".lower() in url:
		return VVVS
	if "VVVS".lower() in url:
		return VVVS
	
	if "other_v_t".lower() in url:
		return VVVT
	if "VVVT".lower() in url:
		return VVVT
	
	if "ward_t".lower() in url:
		return VVVW
	if "VVVW".lower() in url:
		return VVVW
	
	if "other_v_x".lower() in url:
		return VVVX
	if "VVVX".lower() in url:
		return VVVX

	if "OK".lower() in url: #
		return VVA

	return url