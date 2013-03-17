 # -*- coding: utf-8 -*-
# PEP8:OK, LINT:OK, PY3:OK


#############################################################################
## This file may be used under the terms of the GNU General Public
## License version 2.0 or 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http:#www.fsf.org/licensing/licenses/info/GPLv2.html and
## http:#www.gnu.org/copyleft/gpl.html.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################


# metadata
" NINJA-IDE Multimedia "
__version__ = ' 0.1 '
__license__ = ' GPL '
__author__ = ' juancarlospaco '
__email__ = ' juancarlospaco@ubuntu.com '
__url__ = ''
__date__ = ' 20/04/2013 '
__prj__ = ' multimedia '
__docformat__ = 'html'
__source__ = ''
__full_licence__ = ''


# imports
from os import path

from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QDockWidget
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QFileDialog

try:
    from PyKDE4.kdecore import *
    from PyKDE4.kparts import *
except ImportError:
    pass

from ninja_ide.core import plugin


###############################################################################


class Main(plugin.Plugin):
    " dock Class "
    def initialize(self):
        " Init Class dock "
        self.dock = QDockWidget()
        self.dock.setFeatures(QDockWidget.DockWidgetFloatable |
                                           QDockWidget.DockWidgetMovable)
        self.dock.setWindowTitle(__doc__)
        self.dock.setStyleSheet('QDockWidget::title{text-align: center;}')
        self.boton = QPushButton(QIcon.fromTheme("media-eject"),
                                 '  Open Media  ', self.dock)
        try:
            self.factory = KPluginLoader("dragonpart").factory()
            self.part = self.factory.create(self)
            self.boton.clicked.connect(lambda: self.part.openUrl(KUrl(str(
                QFileDialog.getOpenFileName(self.dock, ' Open Media ',
                path.expanduser("~"), ';;'.join(['(*%s)' % e for e in [
                '.ogv', '.webm', '.avi', '.mpg', '.mpeg', '.3gp', '.wmv',
                '.mp3', '.asf', '.dat', '.flv', '.flac', '.ogg', '.mkv',
                '.mov', '.swf', '.wav', '.rm', '.m4v', '.aaf', '.mp4', '.raw'
            ]]))))))
            self.dock.setWidget(self.part.widget())
        except:
            self.dock.setWidget(QLabel(""" <center>
            <h3>ಠ_ಠ<br> ERROR: Please, install Dragon Player App ! </h3><br>
            <br><i> (Sorry, cant embed non-Qt Apps). </i><center>"""))
        self.misc = self.locator.get_service('misc')
        self.misc.add_widget(self.dock,
                        QIcon.fromTheme("applications-multimedia"), __doc__)


###############################################################################


if __name__ == "__main__":
    print(__doc__)
