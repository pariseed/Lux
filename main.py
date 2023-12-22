from jnius import autoclass
from sys import exit

Intent = autoclass('android.content.Intent')
PythonActivity = autoclass('org.kivy.android.PythonActivity')


intent = Intent("com.android.intent.action.SHOW_BRIGHTNESS_DIALOG")
PythonActivity.mActivity.startActivity(intent)
sys.exit(0)
