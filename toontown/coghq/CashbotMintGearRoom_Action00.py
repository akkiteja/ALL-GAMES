from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE07a',
        'wantDoors': 1
    },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None
    },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    10007: {
        'type': 'attribModifier',
        'name': 'goonStrength',
        'comment': '',
        'parentEntId': 0,
        'attribName': 'strength',
        'recursive': 1,
        'typeName': 'goon',
        'value': '10'
    },
    10002: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4.0
    },
    10004: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4
    },
    10006: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10005,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4
    },
    10009: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10008,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4
    },
    10011: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(2.15899157524, 2.2961511611900001, 5.45938539505),
        'hpr': Vec3(331.10910034199998, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 8,
        'rewardPerGrabMax': 0
    },
    10012: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10010,
        'pos': Point3(20.936113357499998, 13.8672618866, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(0.920000016689, 0.920000016689, 0.920000016689),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10013: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10000,
        'pos':
        Point3(57.021869659399997, 5.1502389907800001, 0.0),
        'hpr':
        Vec3(270.0, 0.0, 0.0),
        'scale':
        Vec3(0.66051721572900002, 0.66051721572900002, 0.66051721572900002),
        'collisionsOnly':
        0,
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10015: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(-25.9598789215, 59.441162109399997, 9.7355136871300001),
        'hpr': Vec3(274.08999633799999, 0.0, 0.0),
        'scale': Vec3(1.53790044785, 1.53790044785, 1.53790044785),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_F1.bam'
    },
    10016: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10000,
        'pos':
        Point3(33.339488983199999, -18.3643035889, 0.0),
        'hpr':
        Vec3(180.0, 0.0, 0.0),
        'scale':
        Vec3(0.66000002622599996, 0.66000002622599996, 0.66000002622599996),
        'collisionsOnly':
        0,
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_D1.bam'
    },
    10017: {
        'type':
        'model',
        'name':
        'copy of <unnamed>',
        'comment':
        '',
        'parentEntId':
        10018,
        'pos':
        Point3(0.0, 0.0, 0.0),
        'hpr':
        Point3(169.69999694800001, 0.0, 0.0),
        'scale':
        Vec3(0.90246969461399995, 0.90246969461399995, 0.90246969461399995),
        'collisionsOnly':
        0,
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_D4.bam'
    },
    10020: {
        'type':
        'model',
        'name':
        'copy of <unnamed> (2)',
        'comment':
        '',
        'parentEntId':
        10018,
        'pos':
        Point3(-12.071434021, 0.0, 0.0),
        'hpr':
        Vec3(288.43493652299998, 0.0, 0.0),
        'scale':
        Vec3(0.90246969461399995, 0.90246969461399995, 0.90246969461399995),
        'collisionsOnly':
        0,
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_D4.bam'
    },
    10022: {
        'type':
        'model',
        'name':
        '<unnamed>',
        'comment':
        '',
        'parentEntId':
        10021,
        'pos':
        Point3(-5.9717917442299999, -60.313362121600001, 0.0),
        'hpr':
        Vec3(180.0, 0.0, 0.0),
        'scale':
        Vec3(0.86939114332199996, 0.86939114332199996, 0.86939114332199996),
        'collisionsOnly':
        0,
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10010: {
        'type': 'nodepath',
        'name': 'healPuzzle',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(43.179630279500003, 0.0, 0.0),
        'hpr': Point3(-90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10018: {
        'type': 'nodepath',
        'name': 'rightVertPipes',
        'comment': '',
        'parentEntId': 10021,
        'pos': Point3(-16.4536571503, -45.398178100599999,
                      -8.3999996185299999),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Point3(0.64999997615799998, 0.64999997615799998,
                        1.55999994278)
    },
    10021: {
        'type': 'nodepath',
        'name': 'rightPipes',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10001: {
        'type': 'path',
        'name': 'nearPace',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-59.739196777300002, 0.0, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'pathIndex': 3,
        'pathScale': 1.0
    },
    10003: {
        'type': 'path',
        'name': 'bowtie',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-40.0336875916, 0.0, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'pathIndex': 2,
        'pathScale': 1.0
    },
    10005: {
        'type': 'path',
        'name': 'bridgePace',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-8.8061819076500001, -1.5122487545000001, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'pathIndex': 3,
        'pathScale': 1.0
    },
    10008: {
        'type': 'path',
        'name': 'farPace',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(7.5265827179000002, 7.56240034103, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'pathIndex': 3,
        'pathScale': 1.0
    }
}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}