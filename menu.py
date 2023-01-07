import nuke

nuke.pluginAddPath('./icons')

mamomenu = nuke.menu('Nodes').addMenu(
    'mamoworld', icon='Mamoworld.png')

mochamenu = nuke.menu('Nodes').addMenu(
    'mamoworld/MochaImportPlus', icon='MochaImport.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Stabilized View+',
    'mochaimport.createStabilizedView()',
    icon='MiStabilizedView.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/CornerPin+ w. Lens Dist.',
    'mochaimport.createCornerPin()',
    icon='MiCornerPin.png')

mochamenu.addSeparator()

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Tracker+',
    'mochaimport.createTracker4Node()',
    icon='MiTracker4.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Tracker+ (old)',
    'mochaimport.createTracker3Node()',
    icon='MiTracker3.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/RotoPaint+',
    'mochaimport.createRotoPaintNodeMI()',
    icon='MiRotoPaint.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Roto+',
    'mochaimport.createRotoNodeMI()',
    icon='MiRoto.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/GridWarp+',
    'mochaimport.createGridWarpNodeMI()',
    icon='MiGridWarp.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/SplineWarp+',
    'mochaimport.createSplineWarpNodeMI()',
    icon='MiSplineWarp.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Transform+',
    'mochaimport.createTransformNodeMI()',
    icon='MiMove.png')

mochamenu.addSeparator()

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Camera and Geo+',
    'mochaimport.createCameraAndPointCloud()',
    icon='MiCameraAndGeo.png')

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Full camera rig+',
    'mochaimport.createCameraRig()',
    icon='MiFullCameraRig.png')

mochamenu.addSeparator()

nuke.menu('Nodes').addCommand(
    'mamoworld/MochaImportPlus/Settings',
    'mochaimport.showSettings()',
    icon='MiSettings.png')
