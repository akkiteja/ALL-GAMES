from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE13a',
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
    10001: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(135.90512085, -2.0672273635899998, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'cellId': 0,
        'radius': 10.0
    },
    10003: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-86.735092163100006, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(0.37820470333099998, 2.94127488136, 2.8085868358599999),
        'cellId': 1,
        'radius': 10
    },
    10005: {
        'type': 'model',
        'name': 'farLeft',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(45.6502952576, 31.864765167200002, 0.22889910638300001),
        'hpr': Vec3(333.43493652299998, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10006: {
        'type': 'model',
        'name': 'farRight',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(50.055957794199998, -32.760971069299998,
                      0.22889910638300001),
        'hpr': Vec3(206.56504821799999, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10008: {
        'type': 'model',
        'name': 'nearLeft',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(-47.9696311951, 31.864765167200002, 0.22889910638300001),
        'hpr': Vec3(26.565052032499999, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_D1.bam'
    },
    10009: {
        'type':
        'model',
        'name':
        'nearRight',
        'comment':
        '',
        'parentEntId':
        10004,
        'pos':
        Point3(-43.638748168900001, -36.888355255100002, 0.22889910638300001),
        'hpr':
        Vec3(154.0, 0.0, 0.0),
        'scale':
        Vec3(1.0, 1.0, 1.0),
        'collisionsOnly':
        0,
        'loadType':
        'loadModelCopy',
        'modelPath':
        'phase_10/models/cashbotHQ/pipes_D1.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(102.42070007300001, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10002: {
        'type': 'nodepath',
        'name': 'frontCogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-94.445335388199993, 0.0, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10004: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10007: {
        'type': 'nodepath',
        'name': 'leftCogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 40.958465576199998, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10010: {
        'type': 'nodepath',
        'name': 'rightCogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, -40.959999084499998, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    }
}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [Scenario0]}