# TODO:
# - fix configure arguments (+ compare with FC)
# - create CoinMP library package for PLD (https://projects.coin-or.org/CoinMP)
#
# NOTE - FIXME FOR 3.4.3 !!!:
#	- normal build (i686) requires about 27 GB of disk space:
#		$BUILD_ROOT	7.0 GB
#		BUILD		18  GB
#		RPMS		1.8 GB
#		SRPMS		0.4 GB
#
# Conditional build:
%bcond_without	java		# without Java support (disables help support)
%bcond_without	kde4		# KDE4 L&F packages
%bcond_without	gtk		# GTK2 L&F
%bcond_with	gtk3		# GTK3 L&F (experimental)
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla components
%bcond_without	i18n		# do not create i18n packages (extra build time)
%bcond_with	ccache		# use ccache to speed up builds
%bcond_with	icecream	# use icecream to speed up builds
%bcond_with	msaccess	# with ms access import pieces
%bcond_without	parallelbuild	# use greater number of jobs to speed up build (default: 1)
%bcond_with     tests

%bcond_without	system_beanshell
%bcond_without	system_db		# without system (i.e. with internal) Berkeley DB
%bcond_with	system_coinmp		# use system CoinMP library (not in PLD yet)
%bcond_with	system_libhnj		# with system ALTLinuxhyph (NFY)
%bcond_without	system_mdbtools		# with system mdbtools
%bcond_without	system_xalan
%bcond_with	system_hsqldb
%bcond_with	system_agg		# with system agg
%bcond_without	system_hunspell
%bcond_without	system_myspell

# this list is same as icedtea6
%ifnarch i486 i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_java
%endif

%if %{without java}
%undefine	with_system_beanshell
%undefine	with_system_xalan
%undefine	with_system_hsqldb
%endif

%define		major_ver		6.0.5

Summary:	LibreOffice - powerful office suite
Summary(pl.UTF-8):	LibreOffice - potężny pakiet biurowy
Name:		libreoffice
Version:	%{major_ver}.2
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-%{version}.tar.xz
# Source0-md5:	04e50cf96598790feada18cbeea7bf1f
Source1:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-dictionaries-%{version}.tar.xz
# Source1-md5:	53807d4d8f75d0ea514c0a7fec35431f
Source2:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-help-%{version}.tar.xz
# Source2-md5:	1327c6fd9f65136f905a1b26ba9076b8
Source3:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-translations-%{version}.tar.xz
# Source3-md5:	5f77cd5eff3fc5b84b963d760d7af071


# make (download|fetch) DO_FETCH_TARBALLS=1 WGET=wget
# but not sure if all are needed?
Source20:	http://dev-www.libreoffice.org/src/pdfium-3235.tar.bz2
# Source20-md5:	a7c08f44c6e2e1d7a71f7073cb9d5786
Source21:	http://dev-www.libreoffice.org/src/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
# Source21-md5:	17410483b5b5f267aa18b7e00b65e6e0
Source22:	http://dev-www.libreoffice.org/src/CoinMP-1.7.6.tgz
# Source22-md5:	1cce53bf4b40ae29790d2c5c9f8b1129
Source23:	http://dev-www.libreoffice.org/src/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
# Source23-md5:	798b2ffdc8bcfe7bca2cf92b62caf685
Source24:	http://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
# Source24-md5:	0168229624cfac409e766913506961a8
Source25:	http://dev-www.libreoffice.org/src/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
# Source25-md5:	35c94d2df8893241173de1d16b6034c0
Source26:	https://dev-www.libreoffice.org/extern/odfvalidator-1.2.0-incubating-SNAPSHOT-jar-with-dependencies+ODFTOOLKIT-460+ODFTOOLKIT-461.jar
# Source26-md5:	f430ee376fea2bee62c8510d8b94e813
Source27:	http://dev-www.libreoffice.org/src/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
# Source27-md5:	a7983f859eafb2677d7ff386a023bc40

Patch0:		disable-failing-test.patch
Patch1:         python.patch

URL:		http://www.documentfoundation.org/
BuildRequires:	/usr/bin/getopt
BuildRequires:	Firebird-devel >= 3.0.0.0
BuildRequires:	GConf2-devel
BuildRequires:	GLM
BuildRequires:	ImageMagick
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%{?with_system_agg:BuildRequires:	agg-devel}
BuildRequires:	atk-devel >= 1:1.9.0
BuildRequires:	autoconf >= 2.51
BuildRequires:	automake >= 1:1.9
BuildRequires:	bash
BuildRequires:	bison >= 1.875-4
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cairo-devel >= 1.2.0
%{?with_ccache:BuildRequires:	ccache}
BuildRequires:	clucene-core-devel >= 2.3
%{?with_system_coinmp:BuildRequires:	coinmp-devel}
BuildRequires:	cppunit-devel >= 1.12.0
BuildRequires:	cups-devel
BuildRequires:	curl-devel >= 7.9.8
%{?with_system_db:BuildRequires:	db-devel}
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	gdb
BuildRequires:	glew-devel >= 1.10.0
BuildRequires:	glib2-devel >= 2.13.5
BuildRequires:	gperf
BuildRequires:	gpgme-c++-devel
BuildRequires:	graphite2-devel
BuildRequires:	gstreamer0.10-devel >= 0.10.0
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.0
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.10}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	harfbuzz-icu-devel
%{?with_system_hunspell:BuildRequires:	hunspell-devel >=1.2.2}
BuildRequires:	hyphen-devel
%{?with_icecream:BuildRequires:	icecream}
BuildRequires:	icu
%{?with_system_beanshell:BuildRequires:	java-beanshell}
BuildRequires:	java-commons-codec
BuildRequires:	java-commons-httpclient
BuildRequires:	java-commons-lang
BuildRequires:	java-commons-logging
BuildRequires:	java-flow-engine
BuildRequires:	java-hamcrest
%{?with_system_hsqldb:BuildRequires:	java-hsqldb}
BuildRequires:	java-junit
BuildRequires:	java-lucene
BuildRequires:	java-lucene-contrib
BuildRequires:	java-servletapi
BuildRequires:	libabw-devel >= 0.1.0
BuildRequires:	libe-book-devel >= 0.0.2
BuildRequires:	libetonyek-devel >= 0.1.4
BuildRequires:	libfreehand-devel >= 0.1.0
BuildRequires:	liblangtag-devel
BuildRequires:	libmspub-devel
BuildRequires:	libmwaw-devel >= 0.3.0
BuildRequires:	libodfgen-devel >= 0.1.1
BuildRequires:	liborcus-devel >= 0.13.3
BuildRequires:	libpagemaker-devel >= 0.0.2
BuildRequires:	libstaroffice-devel
BuildRequires:	libvisio-devel
BuildRequires:	libwpd-devel >= 0.10.0
BuildRequires:	libwpg-devel >= 0.3.0
BuildRequires:	libwps-devel >= 0.3.0
BuildRequires:	libzmf-devel
BuildRequires:	lp_solve-devel
BuildRequires:	silgraphite-devel
%if %{with kde4}
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
%endif
BuildRequires:	java-libxml
BuildRequires:	java-sac
%{?with_system_xalan:BuildRequires:	java-xalan}
%{?with_system_xalan:BuildRequires:	java-xalan}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonobo-devel >= 2.0
BuildRequires:	libcdr-devel >= 0.0.8
BuildRequires:	libcmis-devel >= 0.5
BuildRequires:	libepubgen-devel >= 0.1.0
BuildRequires:	libexttextcat-devel
BuildRequires:	libgltf-devel < 0.2.0
BuildRequires:	libgltf-devel >= 0.1.0
%{?with_system_libhnj:BuildRequires:	libhnj-devel}
BuildRequires:	libicu-devel >= 4.0
BuildRequires:	libjpeg-devel
BuildRequires:	libqxp-devel
BuildRequires:	librsvg-devel >= 2.14
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libsvg-devel >= 0.1.4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
%{?with_access:%{?with_system_mdbtools:BuildRequires:	mdbtools-devel >= 0.6}}
BuildRequires:	mdds-devel >= 1.2
%{?with_mono:BuildRequires:	mono-csharp >= 1.2.3}
%{?with_mono:BuildRequires:	mono-static >= 1.2.3}
%{?with_system_myspell:BuildRequires:	myspell-devel}
BuildRequires:	mythes-devel
BuildRequires:	nas-devel >= 1.7-1
BuildRequires:	neon-devel
BuildRequires:	nspr-devel >= 1:4.6-0.20041030.3
BuildRequires:	nss-devel >= 1:3.10
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	pango-devel >= 1:1.17.3
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-base
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-cpp-devel >= 0.8.0
BuildRequires:	poppler-devel >= 0.8.0
BuildRequires:	portaudio-devel
BuildRequires:	postgresql-devel
BuildRequires:	python3 >= 3.3
BuildRequires:	python3-devel >= 3.3
BuildRequires:	python3-modules >= 3.3
BuildRequires:	redland-devel >= 1.0.16
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.660
BuildRequires:	sablotron-devel
BuildRequires:	sane-backends-devel
BuildRequires:	saxon
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	unixODBC-devel >= 2.2.12-2
BuildRequires:	unzip
BuildRequires:	vigra-devel
BuildRequires:	xmlsec1-nss-devel >= 1.2.24
BuildRequires:	xorg-font-font-adobe-utopia-type1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zip >= 3.0
BuildRequires:	zlib-devel
%if %{with java}
BuildRequires:	ant >= 1.7.0
BuildRequires:	ant-apache-regexp
BuildRequires:	jdk >= 1.4.0_00
BuildRequires:	jre-X11
%endif
# contains (dlopened) *.so libs
BuildConflicts:	java-gcj-compat
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-calc = %{version}-%{release}
Requires:	%{name}-draw = %{version}-%{release}
Requires:	%{name}-emailmerge = %{version}-%{release}
Requires:	%{name}-graphicfilter = %{version}-%{release}
Requires:	%{name}-impress = %{version}-%{release}
Requires:	%{name}-math = %{version}-%{release}
Requires:	%{name}-pdfimport = %{version}-%{release}
Requires:	%{name}-postgresql = %{version}-%{release}
Requires:	%{name}-pyuno = %{version}-%{release}
Requires:	%{name}-web = %{version}-%{release}
Requires:	%{name}-wiki-publisher = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Requires:	%{name}-xsltfilter = %{version}-%{release}
Obsoletes:	libreoffice-testtools
Obsoletes:	openoffice.org
Obsoletes:	openoffice.org-testtools
ExclusiveArch:	%{ix86} %{x8664} ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing -O2
%define		filterout_c	-fomit-frame-pointer
%define		filterout_cpp	-fomit-frame-pointer
%define		filterout_cxx	-fomit-frame-pointer

# No ELF objects there to strip/chrpath, skips processing:
# - share/ - 17000 files of 415M
# - help/ - 6500 files of 1.4G
# - program/resource/ - 5610 files of 216M
%define		_noautostrip	.*%{_datadir}/.*
%define		_noautochrpath	.*%{_datadir}/.*

%description
LibreOffice is an open-source project sponsored by Sun Microsystems
and hosted by CollabNet. In October of 2000, Sun released the source
code of its popular StarOfficeTM productivity suite under open-source
licenses. The aim of the LibreOffice project is to create, using
open-source methods, the next generation of open-network productivity
services, including the establishment of open, XML-based standards for
office productivity file formats and language-independent bindings to
component APIs.

Features of LibreOffice include:
 - Downloadable source code,
 - CVS control, and
 - Infrastructure for community involvement, including guidelines and
   discussion groups.

%description -l pl.UTF-8
LibreOffice jest projektem open-source sponsorowanym przez Sun
Microsystems i przechowywanym przez CollabNet. W październiku 2000
roku Sun udostępnił kod źródłowy popularnego pakietu biurowego
StarOfficeTM na zasadach licencji open-source. Głównym celem
LibreOffice jest stworzenie sieciowego pakietu biurowego następnej
generacji, wykorzystując open-source'owe metody pracy.

Do zalet LibreOffice można zaliczyć:
 - dostępny cały czas kod źródłowy,
 - kontrola CVS,
 - infrastruktura służąca do komunikowania się w ramach projektu.

%package libs-kde
Summary:	LibreOffice KDE Interface
Summary(pl.UTF-8):	Interfejs KDE dla LibreOffice
Group:		X11/Libraries
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-kde
Obsoletes:	openoffice-libs-kde
Obsoletes:	openoffice.org-libs-kde

%description libs-kde
LibreOffice productivity suite - KDE Interface.

%description libs-kde -l pl.UTF-8
Pakiet biurowy LibreOffice - Interfejs KDE.

%package libs-gtk
Summary:	LibreOffice GTK+ Interface
Summary(pl.UTF-8):	Interfejs GTK+ dla LibreOffice
Group:		X11/Libraries
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-libs-gtk
Obsoletes:	openoffice.org-libs-gtk

%description libs-gtk
LibreOffice productivity suite - GTK+ Interface.

%description libs-gtk -l pl.UTF-8
Pakiet biurowy LibreOffice - Interfejs GTK+.

%package core
Summary:	Core modules for LibreOffice
Summary(pl.UTF-8):	Podstawowe moduły dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	%{name}-ure = %{version}-%{release}
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
Requires:	fonts-TTF-OpenSymbol
Requires:	hicolor-icon-theme
%{?with_system_beanshell:Requires: java-beanshell}
%{?with_system_hsqldb:Requires: java-hsqldb}
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	saxon
Requires:	sed
%{?with_system_xalan:Requires: xalan-j}
#Suggests: chkfontpath
Obsoletes:	libreoffice-binfilter < 4.0.0.0
Obsoletes:	libreoffice-i18n-kid
Obsoletes:	libreoffice-i18n-ku
Obsoletes:	libreoffice-i18n-ky
Obsoletes:	libreoffice-i18n-ms
Obsoletes:	libreoffice-i18n-pap
Obsoletes:	libreoffice-i18n-ps
Obsoletes:	libreoffice-i18n-qtz
Obsoletes:	libreoffice-i18n-sc
Obsoletes:	libreoffice-i18n-sh
Obsoletes:	libreoffice-i18n-ti
Obsoletes:	libreoffice-i18n-ur
Obsoletes:	libreoffice-javafilter < 4.1.0.0
Obsoletes:	libreoffice-report-builder < 4.1.0.0
Obsoletes:	oooqs
Obsoletes:	openoffice
Obsoletes:	openoffice-i18n-fo
Obsoletes:	openoffice-i18n-fo-gtk
Obsoletes:	openoffice-i18n-ia
Obsoletes:	openoffice-i18n-ia-gtk
Obsoletes:	openoffice-i18n-id
Obsoletes:	openoffice-i18n-id-gtk
Obsoletes:	openoffice-i18n-la
Obsoletes:	openoffice-i18n-la-gtk
Obsoletes:	openoffice-i18n-med
Obsoletes:	openoffice-i18n-med-gtk
Obsoletes:	openoffice-i18n-mi
Obsoletes:	openoffice-i18n-mi-gtk
Obsoletes:	openoffice-i18n-ro
Obsoletes:	openoffice-i18n-ro-gtk
Obsoletes:	openoffice-libs
Obsoletes:	openoffice.org-core
Obsoletes:	openoffice.org-dirs
Obsoletes:	openoffice.org-i18n-bn_BD
Obsoletes:	openoffice.org-i18n-by
Obsoletes:	openoffice.org-i18n-fo
Obsoletes:	openoffice.org-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-kde
Obsoletes:	openoffice.org-i18n-gu_IN
Obsoletes:	openoffice.org-i18n-ia
Obsoletes:	openoffice.org-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-kde
Obsoletes:	openoffice.org-i18n-id
Obsoletes:	openoffice.org-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-kde
Obsoletes:	openoffice.org-i18n-kid
Obsoletes:	openoffice.org-i18n-ky
Obsoletes:	openoffice.org-i18n-la
Obsoletes:	openoffice.org-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-kde
Obsoletes:	openoffice.org-i18n-med
Obsoletes:	openoffice.org-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-kde
Obsoletes:	openoffice.org-i18n-mi
Obsoletes:	openoffice.org-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-kde
Obsoletes:	openoffice.org-i18n-ms
Obsoletes:	openoffice.org-i18n-pap
Obsoletes:	openoffice.org-i18n-ro
Obsoletes:	openoffice.org-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-kde
Obsoletes:	openoffice.org-i18n-sc
Obsoletes:	openoffice.org-i18n-sw
Obsoletes:	openoffice.org-i18n-sx
Obsoletes:	openoffice.org-i18n-ti
Obsoletes:	openoffice.org-i18n-ur
Obsoletes:	openoffice.org-libs < 1:2.1.0-0.m6.0.11

%description core
Core libraries and support files for LibreOffice.

%description core -l pl.UTF-8
Podstawowe moduły dla LibreOffice.

%package pyuno
Summary:	Python bindings for LibreOffice
Summary(pl.UTF-8):	Wiązania Pythona dla LibreOffice
Group:		Libraries
Requires:	%{name}-core = %{version}-%{release}
Requires:	python
Provides:	pyuno
Obsoletes:	openoffice.org-pyuno

%description pyuno
Cool Python bindings for the LibreOffice UNO component model. Allows
scripts both external to LibreOffice and within the internal
LibreOffice scripting module to be written in Python.

%description pyuno -l pl.UTF-8
Wiązania Pythona dla modelu komponentów UNO LibreOffice. Pozwala na
oskryptowanie zarówno na zewnątrz LibreOffice, jak i na używanie
skryptów w Pythonie w wewnętrznym module skryptów LibreOffice.

%package pdfimport
Summary:	PDF Importer for LibreOffice Draw
Group:		X11/Applications
Requires:	%{name}-draw = %{version}-%{release}

%description pdfimport
The PDF Importer imports PDF into drawing documents to preserve layout
and enable basic editing of PDF documents.

%package wiki-publisher
Summary:	Create Wiki articles on MediaWiki servers with LibreOffice
Group:		X11/Applications
Requires:	%{name}-writer = %{version}-%{release}
Requires:	java-commons-codec
Requires:	java-commons-httpclient
Requires:	java-commons-lang
Requires:	java-commons-logging
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki
servers without having to know the syntax of the MediaWiki markup
language. Publish your new and existing documents transparently with
writer to a wiki page.

%package base
Summary:	Database frontend for LibreOffice
Summary(pl.UTF-8):	Frontend do baz danych dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-base

%description base
GUI database frontend for LibreOffice. Allows creation and management
of databases through a GUI.

%description base -l pl.UTF-8
Graficzny frontend do baz danych dla LibreOffice. Pozwala na tworzenie
i zarządzanie bazami poprzez graficzny interfejs użytkownika.

%package web
Summary:	Web module for LibreOffice
Summary(pl.UTF-8):	Moduł Web dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Obsoletes:	openoffice.org-web

%description web
Web publishing application of LibreOffice.

%description web -l pl.UTF-8
Aplikacja do tworzenia stron WWW z LibreOffice.

%package writer
Summary:	Writer module for LibreOffice
Summary(pl.UTF-8):	Moduł Writer dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-writer

%description writer
Wordprocessor application of LibreOffice.

%description writer -l pl.UTF-8
Procesor tekstu z LibreOffice.

%package emailmerge
Summary:	email mail merge component for LibreOffice
Summary(pl.UTF-8):	Kompolent email mail merge dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-pyuno = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Obsoletes:	openoffice.org-emailmerge

%description emailmerge
Enables LibreOffice Writer module to enable mail merge to email.

%description emailmerge -l pl.UTF-8
Komponent umożliwiający modułowi Writer włączanie poczty do poczty
elektronicznej.

%package calc
Summary:	Calc module for LibreOffice
Summary(pl.UTF-8):	Moduł Calc dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-calc

%description calc
Spreadsheet application of LibreOffice.

%description calc -l pl.UTF-8
Arkusz kalkulacyjny z LibreOffice.

%package draw
Summary:	Draw module for LibreOffice
Summary(pl.UTF-8):	Moduł Draw dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-draw

%description draw
Drawing application of LibreOffice.

%description draw -l pl.UTF-8
Aplikacja rysunkowa z LibreOffice.

%package impress
Summary:	Impress module for LibreOffice
Summary(pl.UTF-8):	Moduł Impress dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	libreoffice-presentation-minimizer < 4.2.0.0
Obsoletes:	libreoffice-presenter-screen < 4.0.0.0-1
Obsoletes:	openoffice.org-impress

%description impress
Presentation application of LibreOffice.

%description impress -l pl.UTF-8
Aplikacja do tworzenia prezentacji z LibreOffice.

%package math
Summary:	Math module for LibreOffice
Summary(pl.UTF-8):	Moduł Math dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-math

%description math
Math editor of LibreOffice.

%description math -l pl.UTF-8
Edytor równań matematycznych z LibreOffice.

%package graphicfilter
Summary:	Extra graphicfilter module for LibreOffice
Summary(pl.UTF-8):	Dodatkowy moduł graphicfilter dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-graphicfilter

%description graphicfilter
Graphicfilter module for LibreOffice, provides additional SVG and
Flash export filters.

%description graphicfilter -l pl.UTF-8
Moduł graphicfilter dla LibreOffice, udostępnia dodatkowe filtry
eksportu SVG i Flash.

%package xsltfilter
Summary:	Extra xsltfilter module for LibreOffice
Summary(pl.UTF-8):	Dodatkowy moduł xsltfilter dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-xsltfilter

%description xsltfilter
xsltfilter module for LibreOffice, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%description xsltfilter -l pl.UTF-8
Moduł xsltfilter dla LibreOffice, udostępnia dodatkowe przekształcenia
wyjściowe dla formatów docbook i xhtml. Jest potrzebny do eksportu do
docbooka.

%package postgresql
Summary:	PostgreSQL connector for LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	postgresql-libs

%description postgresql
A PostgreSQL connector for the database front-end for LibreOffice.
Allows creation and management of PostgreSQL databases through a GUI.

%package nlpsolver
Summary:	Non-linear solver engine for LibreOffice Calc
Group:		X11/Applications
Requires:	%{name}-calc = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-ure = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description nlpsolver
A non-linear solver engine for Calc as an alternative to the default
linear programming model when more complex, nonlinear programming is
required.

# FIXME
%package ure
Summary:	UNO Runtime Environment
Group:		Libraries
Obsoletes:	openoffice.org-ure

%description ure
UNO is the component model of LibreOffice. UNO offers interoperability
between programming languages, other components models and hardware
architectures, either in process or over process boundaries, in the
Intranet as well as in the Internet. UNO components may be implemented
in and accessed from any programming language for which a UNO
implementation (AKA language binding) and an appropriate bridge or
adapter exists.

%package -n browser-plugin-%{name}
Summary:	LibreOffice plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka LibreOffice dla przeglądarek WWW
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	browser-plugin-openoffice.org

%description -n browser-plugin-%{name}
LibreOffice plugin for WWW browsers.

This plugin allows browsers to display OOo documents inline.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka LibreOffice dla przeglądarek WWW.

Ta wtyczka umożliwia wyświetlanie dokumentów OOo wewnątrz stron.

%package i18n-af
Summary:	LibreOffice - interface in Afrikaans language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku afrykanerskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af
Obsoletes:	openoffice.org-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
afrykanerskim.

%package i18n-am
Summary:	LibreOffice - interface in Amharic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku amharskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-am
This package provides resources containing menus and dialogs in
Amharic language.

%description i18n-am -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
amharskim.

%package i18n-ar
Summary:	LibreOffice - interface in Arabic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku arabskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar
Obsoletes:	openoffice.org-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ar
This package provides resources containing menus and dialogs in Arabic
language.

%description i18n-ar -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
arabskim.

%package i18n-as
Summary:	LibreOffice - interface in Assamese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku asamskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-as_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-as
This package provides resources containing menus and dialogs in
Assamese language.

%description i18n-as -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
asamskim.

%package i18n-ast
Summary:	LibreOffice - interface in Asturian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku asturyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ast
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ast
This package provides resources containing menus and dialogs in
Asturian language.

%description i18n-ast -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
asturyjskim.

%package i18n-be_BY
Summary:	LibreOffice - interface in Belarusian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku białoruskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-be_BY
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-be_BY
This package provides resources containing menus and dialogs in
Belarusian language.

%description i18n-be_BY -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
białoruskim.

%package i18n-bg
Summary:	LibreOffice - interface in Bulgarian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bułgarskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-bg
Obsoletes:	openoffice-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg
Obsoletes:	openoffice.org-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bułgarskim.

%package i18n-bn_IN
Summary:	LibreOffice - interface in Indian Bangla language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku indyjskim bengalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bn_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-bn_IN
This package provides resources containing menus and dialogs in Indian
Bangla language.

%description i18n-bn_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
indyjskim bengalskim.

%package i18n-bn
Summary:	LibreOffice - interface in Bangla language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bengalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bn
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-bn
This package provides resources containing menus and dialogs in Bangla
language.

%description i18n-bn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bengalskim.

%package i18n-bo
Summary:	LibreOffice - interface in Tibetan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tybetańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bo
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-bo
This package provides resources containing menus and dialogs in
Tibetan language.

%description i18n-bo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tybetańskim.

%package i18n-br
Summary:	LibreOffice - interface in Breton language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bretońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-br
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-br
This package provides resources containing menus and dialogs in Breton
language.

%description i18n-br -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bretońskim.

%package i18n-brx
Summary:	LibreOffice - interface in Bodo language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku boro
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-brx
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-brx
This package provides resources containing menus and dialogs in Bodo
language.

%description i18n-brx -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
boro.

%package i18n-bs
Summary:	LibreOffice - interface in Bosnian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bośniackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bs
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-bs
This package provides resources containing menus and dialogs in
Bosnian language.

%description i18n-bs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bośniackim.

%package i18n-ca
Summary:	LibreOffice - interface in Catalan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku katalońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ca
Obsoletes:	openoffice-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca
Obsoletes:	openoffice.org-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
katalońskim.

%package i18n-ca_XV
Summary:	LibreOffice - interface in Catalan Valencian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku katalońskim walenckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ca_XV
This package provides resources containing menus and dialogs in
Catalan Valencian language.

%description i18n-ca_XV -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
katalońskim walenckim.

%package i18n-cs
Summary:	LibreOffice - interface in Czech language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku czeskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs
Obsoletes:	openoffice.org-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-cs
This package provides resources containing menus and dialogs in Czech
language.

%description i18n-cs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
czeskim.

%package i18n-cy
Summary:	LibreOffice - interface in Cymraeg language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku walijskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-cy
Obsoletes:	openoffice-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy
Obsoletes:	openoffice.org-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-cy
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
walijskim.

%package i18n-da
Summary:	LibreOffice - interface in Danish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku duńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-da
Obsoletes:	openoffice-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da
Obsoletes:	openoffice.org-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-da
This package provides resources containing menus and dialogs in Danish
language.

%description i18n-da -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
duńskim.

%package i18n-de
Summary:	LibreOffice - interface in German language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku niemieckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-de
Obsoletes:	openoffice-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de
Obsoletes:	openoffice.org-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-de
This package provides resources containing menus and dialogs in German
language.

%description i18n-de -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
niemieckim.

%package i18n-dgo
Summary:	LibreOffice - interface in Dogri language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku dogri
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-dgo
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-dgo
This package provides resources containing menus and dialogs in Dogri
language.

%description i18n-dgo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
dogri.

%package i18n-dz
Summary:	LibreOffice - interface in Dzongkha language
Summary(pl.UTF-8):	Openoffice.org - interfejs w języku dżongkha
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-dz
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-dz
This package provides resources containing menus and dialogs in
Dzongkha language.

%description i18n-dz -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
dżongkha.

%package i18n-el
Summary:	LibreOffice - interface in Greek language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku greckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-el
Obsoletes:	openoffice-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el
Obsoletes:	openoffice.org-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-el
This package provides resources containing menus and dialogs in Greek
language.

%description i18n-el -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
greckim.

%package i18n-en_GB
Summary:	LibreOffice - interface in English language for United Kingdom
Summary(pl.UTF-8):	LibreOffice - interfejs w języku anglieskim dla Wielkiej Brytanii
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-en_GB
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-en_GB
This package provides resources containing menus and dialogs in
English language for United Kingdom.

%description i18n-en_GB -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
anglieskim dla Wielkiej Brytanii.

%package i18n-en_ZA
Summary:	LibreOffice - interface in English language for South Africa
Summary(pl.UTF-8):	LibreOffice - interfejs w języku anglieskim dla Południowej Afryki
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-en_ZA
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-en_ZA
This package provides resources containing menus and dialogs in
English language for South Africa.

%description i18n-en_ZA -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
anglieskim dla Południowej Afryki.

%package i18n-eo
Summary:	LibreOffice - interface in Esperanto language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku esperanto
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-eo
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-eo
This package provides resources containing menus and dialogs in
Esperanto language.

%description i18n-eo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
esperanto.

%package i18n-es
Summary:	LibreOffice - interface in Spanish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku hiszpańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-es
Obsoletes:	openoffice-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es
Obsoletes:	openoffice.org-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hiszpańskim.

%package i18n-et
Summary:	LibreOffice - interface in Estonian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku estońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-et
Obsoletes:	openoffice-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et
Obsoletes:	openoffice.org-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-et
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
estońskim.

%package i18n-eu
Summary:	LibreOffice - interface in Basque (Euskara) language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku baskijskim (euskera)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-eu
Obsoletes:	openoffice-i18n-eu-gtk
Obsoletes:	openoffice-i18n-eu-kde
Obsoletes:	openoffice.org-i18n-eu
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-eu
This package provides resources containing menus and dialogs in Basque
(Euskara) language.

%description i18n-eu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
baskijskim (euskera).

%package i18n-fa
Summary:	LibreOffice - interface in Persian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku perskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fa
Obsoletes:	openoffice-i18n-fa-gtk
Obsoletes:	openoffice-i18n-fa-kde
Obsoletes:	openoffice.org-i18n-fa
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-fa
This package provides resources containing menus and dialogs in
Persian language.

%description i18n-fa -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
perskim.

%package i18n-fi
Summary:	LibreOffice - interface in Finnish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku fińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi
Obsoletes:	openoffice.org-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
fińskim.

%package i18n-fr
Summary:	LibreOffice - interface in French language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku francuskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fr
Obsoletes:	openoffice-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr
Obsoletes:	openoffice.org-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-fr
This package provides resources containing menus and dialogs in French
language.

%description i18n-fr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
francuskim.

%package i18n-ga
Summary:	LibreOffice - interface in Irish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku irlandzkim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ga
Obsoletes:	openoffice-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga
Obsoletes:	openoffice.org-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ga
This package provides resources containing menus and dialogs in Irish
language.

%description i18n-ga -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
irlandzkim.

%package i18n-gd
Summary:	LibreOffice - interface in Scottish Gaelic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku gaelickim szkockim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-gd
This package provides resources containing menus and dialogs in
Scottish Gaelic language.

%description i18n-gd -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gaelicki szkocki.

%package i18n-gl
Summary:	LibreOffice - interface in Galician language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku galicyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl
Obsoletes:	openoffice.org-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-gl
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
galicyjskim.

%package i18n-gu
Summary:	LibreOffice - interface in Gujarati language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku gudźarati
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-gu
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-gu
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gudźarati.

%package i18n-gug
Summary:	LibreOffice - interface in Paraguayan Gujarati language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku paragwajskim gudźarati
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-gug
This package provides resources containing menus and dialogs in
Paraguayan Gujarati language.

%description i18n-gug -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
paragwajskim gudźarati.

%package i18n-he
Summary:	LibreOffice - interface in Hebrew language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku hebrajskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-he
Obsoletes:	openoffice-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he
Obsoletes:	openoffice.org-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-he
This package provides resources containing menus and dialogs in Hebrew
language.

%description i18n-he -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hebrajskim.

%package i18n-hi
Summary:	LibreOffice - interface in Hindi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku hindi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hi
Obsoletes:	openoffice-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-kde
Obsoletes:	openoffice.org-i18n-hi_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-hi
This package provides resources containing menus and dialogs in Hindi
language.

%description i18n-hi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hindi.

%package i18n-hr
Summary:	LibreOffice - interface in Croatian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku chorwackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hr
Obsoletes:	openoffice-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr
Obsoletes:	openoffice.org-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-hr
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chorwackim.

%package i18n-hsb
Summary:	LibreOffice - interface in Upper Sorbian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku górnołużyckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hsb
Obsoletes:	openoffice-i18n-hsb-gtk
Obsoletes:	openoffice.org-i18n-hsb
Obsoletes:	openoffice.org-i18n-hsb-gtk
Obsoletes:	openoffice.org-i18n-hsb-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-hsb
This package provides resources containing menus and dialogs in
Upper Sorbian language.

%description i18n-hsb -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
górnołużycki.

%package i18n-hu
Summary:	LibreOffice - interface in Hungarian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku węgierskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hu
Obsoletes:	openoffice-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu
Obsoletes:	openoffice.org-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
węgierskim.

%package i18n-id
Summary:	LibreOffice - interface in Indonesian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku indonezyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-id
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
indonezyjskim.

%package i18n-is
Summary:	LibreOffice - interface in Icelandic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku islandzkim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-is
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-is
This package provides resources containing menus and dialogs in
Icelandic language.

%description i18n-is -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
islandzkim.

%package i18n-it
Summary:	LibreOffice - interface in Italian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku włoskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-it
Obsoletes:	openoffice-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it
Obsoletes:	openoffice.org-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
włoskim.

%package i18n-ja
Summary:	LibreOffice - interface in Japan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku japońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ja
Obsoletes:	openoffice-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja
Obsoletes:	openoffice.org-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ja
This package provides resources containing menus and dialogs in Japan
language.

%description i18n-ja -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
japońskim.

%package i18n-ka
Summary:	LibreOffice - interface in Georgian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku gruzińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ka
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ka
This package provides resources containing menus and dialogs in
Georgian language.

%description i18n-ka -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gruzińskim.

%package i18n-kk
Summary:	LibreOffice - interface in Kazakh language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kazachskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-kk
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-kk
This package provides resources containing menus and dialogs in Kazakh
language.

%description i18n-kk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kazachskim.

%package i18n-km
Summary:	LibreOffice - interface in Khmer language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku khmerskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-km
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-km
This package provides resources containing menus and dialogs in Khmer
language.

%description i18n-km -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
khmerskim.

%package i18n-kmr-Latn
Summary:	LibreOffice - interface in Kurdisk language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kurdyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-kmr-Latn
This package provides resources containing menus and dialogs in
Kurdish language.

%description i18n-km -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kurdyjskim.

%package i18n-kn_IN
Summary:	LibreOffice - interface in Kannada language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kannara
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-kn
Obsoletes:	openoffice-i18n-kn-gtk
Obsoletes:	openoffice-i18n-kn-kde
Obsoletes:	openoffice.org-i18n-kn_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-kn_IN
This package provides resources containing menus and dialogs in
Kannada language.

%description i18n-kn_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kannara.

%package i18n-ko
Summary:	LibreOffice - interface in Korean language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku koreańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ko
Obsoletes:	openoffice-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko
Obsoletes:	openoffice.org-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ko
This package provides resources containing menus and dialogs in Korean
language.

%description i18n-ko -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
koreańskim.

%package i18n-kok
Summary:	LibreOffice - interface in Konkani language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku konkani
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-kok
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-kok
This package provides resources containing menus and dialogs in
Konkani language.

%description i18n-kok -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
konkani.

%package i18n-ks
Summary:	LibreOffice - interface in Kashmiri language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kaszmirskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ks
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ks
This package provides resources containing menus and dialogs in
Kashmiri language.

%description i18n-ks -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kaszmirskim.

%package i18n-lb
Summary:	LibreOffice - interface in Luxembourgish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku luksemburgskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-lb
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-lb
This package provides resources containing menus and dialogs in
Luxembourgish language.

%description i18n-lb -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
luksemburgskim.

%package i18n-lo
Summary:	LibreOffice - interface in Lao language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku laotańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-lo
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-lo
This package provides resources containing menus and dialogs in Lao
language.

%description i18n-lo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
laotańskim.

%package i18n-lt
Summary:	LibreOffice - interface in Lithuanian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku litewskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-lt
Obsoletes:	openoffice-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt
Obsoletes:	openoffice.org-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-lt
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
litewskim.

%package i18n-lv
Summary:	LibreOffice - interface in Latvian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku łotewskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-lv
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-lv
This package provides resources containing menus and dialogs in
Latvian language.

%description i18n-lv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
łotewskim.

%package i18n-mai
Summary:	LibreOffice - interface in Maithili language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku maithili
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mai
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-mai
This package provides resources containing menus and dialogs in
Maithili language.

%description i18n-mai -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
maithili.

%package i18n-mk
Summary:	LibreOffice - interface in Macedonian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku macedońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mk
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-mk
This package provides resources containing menus and dialogs in
Macedonian language.

%description i18n-mk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
macedońskim.

%package i18n-ml
Summary:	LibreOffice - interface in Malayalam language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku malajalamskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ml_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ml
This package provides resources containing menus and dialogs in
Malayalam language.

%description i18n-ml -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
malajalamskim.

%package i18n-mni
Summary:	LibreOffice - interface in Meitei language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku manipuri
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mni
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-mni
This package provides resources containing menus and dialogs in Meitei
language.

%description i18n-mni -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
manipuri.

%package i18n-mr
Summary:	LibreOffice - interface in Marathi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku marathi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mr_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-mr
This package provides resources containing menus and dialogs in
Marathi language.

%description i18n-mr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
marathi.

%package i18n-mn
Summary:	LibreOffice - interface in Mongolian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku mongolskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mn
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-mn
This package provides resources containing menus and dialogs in
Mongolian language.

%description i18n-mn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
mongolskim.

%package i18n-my
Summary:	LibreOffice - interface in Burmese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku birmańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-my
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-my
This package provides resources containing menus and dialogs in
Burmese language.

%description i18n-my -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
birmańskim.

%package i18n-nb
Summary:	LibreOffice - interface in Norwegian Bokmaal language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku norweskim (odmiana Bokmaal)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nb
Obsoletes:	openoffice-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb
Obsoletes:	openoffice.org-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-nb
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
norweskim w odmianie Bokmaal.

%package i18n-ne
Summary:	LibreOffice - interface in Nepali language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku nepalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ne
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ne
This package provides resources containing menus and dialogs in Nepali
language.

%description i18n-ne -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
nepalskim.

%package i18n-nl
Summary:	LibreOffice - interface in Dutch language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku holenderskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nl
Obsoletes:	openoffice-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl
Obsoletes:	openoffice.org-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-nl
This package provides resources containing menus and dialogs in Dutch
language.

%description i18n-nl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
holenderskim.

%package i18n-nn
Summary:	LibreOffice - interface in Norwegian Nynorsk language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku norweskim (odmiana Nynorsk)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nn
Obsoletes:	openoffice-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn
Obsoletes:	openoffice.org-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-nn
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
norweskim w odmianie Nynorsk.

%package i18n-nr
Summary:	LibreOffice - interface in South Ndebele language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ndebele (południowym)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-nr
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-nr
This package provides resources containing menus and dialogs in South
Ndebele language.

%description i18n-nr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ndebele (południowym).

%package i18n-nso
Summary:	LibreOffice - interface in Northern Sotho language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ludu Soto
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nso
Obsoletes:	openoffice-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso
Obsoletes:	openoffice.org-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-nso
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ludu Soto.

%package i18n-oc
Summary:	LibreOffice - interface in Occitan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku oksytańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-oc
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-oc
This package provides resources containing menus and dialogs in
Occitan language.

%description i18n-oc -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
oksytańskim.

%package i18n-om
Summary:	LibreOffice - interface in Oromo language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku oromo
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-om
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-om
This package provides resources containing menus and dialogs in Oromo
language.

%description i18n-om -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
oromo.

%package i18n-or
Summary:	LibreOffice - interface in Oriya language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku orija
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-or_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-or
This package provides resources containing menus and dialogs in Oriya
language.

%description i18n-or -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
orija.

%package i18n-pa_IN
Summary:	LibreOffice - interface in Punjabi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku pendżabskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-pa_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-pa_IN
This package provides resources containing menus and dialogs in
Punjabi language.

%description i18n-pa_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
pendżabskim.

%package i18n-pl
Summary:	LibreOffice - interface in Polish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku polskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl
Obsoletes:	openoffice.org-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-pl
This package provides resources containing menus and dialogs in Polish
language.

%description i18n-pl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
polskim.

%package i18n-pt
Summary:	LibreOffice - interface in Portuguese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku portugalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt
Obsoletes:	openoffice.org-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim.

%package i18n-pt_BR
Summary:	LibreOffice - interface in Brazilian Portuguese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku portugalskim dla Brazylii
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR
Obsoletes:	openoffice-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR
Obsoletes:	openoffice.org-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim dla Brazylii.

%package i18n-ro
Summary:	LibreOffice - interface in Romanian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku rumuńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ro
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ro
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
rumuńskim.

%package i18n-ru
Summary:	LibreOffice - interface in Russian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku rosyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ru
Obsoletes:	openoffice-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru
Obsoletes:	openoffice.org-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
rosyjskim.

%package i18n-rw
Summary:	LibreOffice - interface in Kinarwanda language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kinya-ruanda
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-rw
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-rw
This package provides resources containing menus and dialogs in
Kinarwanda language.

%description i18n-rw -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kinya-ruanda.

%package i18n-sa_IN
Summary:	LibreOffice - interface in Sanskrit language
Summary(pl.UTF-8):	LibreOffice - interfejs w sanskrycie
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sa_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sa_IN
This package provides resources containing menus and dialogs in
Sanskrit language.

%description i18n-sa_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w
sanskrycie.

%package i18n-sat
Summary:	LibreOffice - interface in Santali language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku santali
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sat
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sat
This package provides resources containing menus and dialogs in
Santali language.

%description i18n-sat -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
santali.

%package i18n-sd
Summary:	LibreOffice - interface in Sindhi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku sindhi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sd
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sd
This package provides resources containing menus and dialogs in Sindhi
language.

%description i18n-sd -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
sindhi.

%package i18n-si
Summary:	LibreOffice - interface in Sinhala language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku syngaleskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-si
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-si
This package provides resources containing menus and dialogs in
Sinhala language.

%description i18n-si -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
syngaleskim.

%package i18n-sid
Summary:	LibreOffice - interface in Sidama language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku sidamo
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sid
This package provides resources containing menus and dialogs in Sidama
language.

%description i18n-sid -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
sidamo.

%package i18n-sk
Summary:	LibreOffice - interface in Slovak language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku słowackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-sk
Obsoletes:	openoffice-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk
Obsoletes:	openoffice.org-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sk
This package provides resources containing menus and dialogs in Slovak
language.

%description i18n-sk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
słowackim.

%package i18n-sl
Summary:	LibreOffice - interface in Slovenian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku słoweńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-sl
Obsoletes:	openoffice-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl
Obsoletes:	openoffice.org-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sl
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
słoweńskim.

%package i18n-sq
Summary:	LibreOffice - interface in Albanian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku albańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sq
This package provides resources containing menus and dialogs in
Albanian language.

%description i18n-sq -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
albańskim.

%package i18n-sr
Summary:	LibreOffice - interface in Serbian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku serbskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sr
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sr
This package provides resources containing menus and dialogs in
Serbian language.

%description i18n-sr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbskim.

%package i18n-sr-Latn
Summary:	LibreOffice - interface in Serbian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku serbskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sr-Latn
This package provides resources containing menus and dialogs in
Serbian language.

%description i18n-sr-Latn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbskim.

%package i18n-ss
Summary:	LibreOffice - interface in Swati language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku suazi (siswati)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ss
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ss
This package provides resources containing menus and dialogs in Swati
language.

%description i18n-ss -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suazi (siswati).

%package i18n-st
Summary:	LibreOffice - interface in Southern Sotho language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku południowym sotho
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-st
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-st
This package provides resources containing menus and dialogs in
Southern Sotho language.

%description i18n-st -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
południowym sotho.

%package i18n-sv
Summary:	LibreOffice - interface in Swedish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku szwedzkim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-sv
Obsoletes:	openoffice-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv
Obsoletes:	openoffice.org-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
szwedzkim.

%package i18n-sw_TZ
Summary:	LibreOffice - interface in Swahili language for Tanzania
Summary(pl.UTF-8):	LibreOffice - interfejs w języku suahili dla Tanzanii
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sw_TZ
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-sw_TZ
This package provides resources containing menus and dialogs in
Swahili language for Tanzania.

%description i18n-sw_TZ -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suahili dla Tanzanii.

%package i18n-ta
Summary:	LibreOffice - interface in Tamil language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tamiskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ta_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ta
This package provides resources containing menus and dialogs in Tamil
language.

%description i18n-ta -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tamilskim.

%package i18n-te
Summary:	LibreOffice - interface in Telugu language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku telugu
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-te_IN
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-te
This package provides resources containing menus and dialogs in Telugu
language.

%description i18n-te -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
telugu.

%package i18n-tg
Summary:	LibreOffice - interface in Tajik language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tadżyckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-tg
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-tg
This package provides resources containing menus and dialogs in Tajik
language.

%description i18n-tg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tadżyckim.

%package i18n-th
Summary:	LibreOffice - interface in Thai language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tajskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-th
Obsoletes:	openoffice-i18n-th-gtk
Obsoletes:	openoffice-i18n-th-kde
Obsoletes:	openoffice.org-i18n-th
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-th
This package provides resources containing menus and dialogs in Thai
language.

%description i18n-th -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tajskim.

%package i18n-tn
Summary:	LibreOffice - interface in Tswana language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tswana
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-tn
Obsoletes:	openoffice-i18n-tn-gtk
Obsoletes:	openoffice-i18n-tn-kde
Obsoletes:	openoffice.org-i18n-tn
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-tn
This package provides resources containing menus and dialogs in Tswana
language.

%description i18n-tn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tswana.

%package i18n-tr
Summary:	LibreOffice - interface in Turkish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tureckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-tr
Obsoletes:	openoffice-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr
Obsoletes:	openoffice.org-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tureckim.

%package i18n-ts
Summary:	LibreOffice - interface in Tsonga language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tsonga
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ts
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ts
This package provides resources containing menus and dialogs in Tsonga
language.

%description i18n-ts -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tsonga.

%package i18n-tt
Summary:	LibreOffice - interface in Tatar language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tatarskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-tt
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-tt
This package provides resources containing menus and dialogs in Tatar
language.

%description i18n-tt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tatarskim.

%package i18n-ug
Summary:	LibreOffice - interface in Uyghur language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ujgurskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ug
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ug
This package provides resources containing menus and dialogs in Uyghur
language.

%description i18n-ug -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ujgurskim.

%package i18n-uk
Summary:	LibreOffice - interface in Ukrainian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ukraińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-uk
Obsoletes:	openoffice-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk
Obsoletes:	openoffice.org-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ukraińskim.

%package i18n-uz
Summary:	LibreOffice - interface in Uzbek language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku uzbeckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-uz
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-uz
This package provides resources containing menus and dialogs in Uzbek.

%description i18n-uz -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
uzbeckim.

%package i18n-ve
Summary:	LibreOffice - interface in Venda language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku venda
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ve
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-ve
This package provides resources containing menus and dialogs in Venda
language.

%description i18n-ve -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
venda.

%package i18n-vi
Summary:	LibreOffice - interface in Vietnamese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku wietnamskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-vi
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-vi
This package provides resources containing menus and dialogs in
Vietnamese language.

%description i18n-vi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
wietnamskim.

%package i18n-xh
Summary:	LibreOffice - interface in Xhosa language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku khosa
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-xh
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-xh
This package provides resources containing menus and dialogs in Xhosa
language.

%description i18n-xh -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
khosa.

%package i18n-zh_CN
Summary:	LibreOffice - interface in Chinese language for China
Summary(pl.UTF-8):	LibreOffice - interfejs w języku chińskim dla Chin
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN
Obsoletes:	openoffice-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN
Obsoletes:	openoffice.org-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chińskim dla Chin.

%package i18n-zh_TW
Summary:	LibreOffice - interface in Chinese language for Taiwan
Summary(pl.UTF-8):	LibreOffice - interfejs w języku chińskim dla Tajwanu
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW
Obsoletes:	openoffice-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW
Obsoletes:	openoffice.org-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chińskim dla Tajwanu.

%package i18n-vec
Summary:	LibreOffice - interface in Venetian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku Venetian
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-vec
This package provides resources containing menus and dialogs in
Venetian language.

%description i18n-vec -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
Venetian.

%package i18n-zu
Summary:	LibreOffice - interface in Zulu language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku zuluskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-zu
Obsoletes:	openoffice-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu
Obsoletes:	openoffice.org-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-kde
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description i18n-zu
This package provides resources containing menus and dialogs in Zulu
language.

%description i18n-zu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
zuluskim.

%package -n bash-completion-%{name}
Summary:	bash-completion for LibreOffice
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla LibreOffice
Group:		Applications/Shells
Requires:	%{name}
Requires:	bash-completion
Obsoletes:	bash-completion-openoffice
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-%{name}
bash-completion for LibreOffice.

%description -n bash-completion-%{name} -l pl.UTF-8
bashowe uzupełnianie nazw dla LibreOffice.

%package glade
Summary:	Support for creating LibreOffice dialogs in glade
Group:		Development/Libraries
Requires:	%{name}-core = %{version}-%{release}
Requires:	libgladeui

%description glade
libreoffice-glade contains a catalog of LibreOffice-specific widgets
for glade and ui-previewer tool to check the visual appearance of
dialogs.

%prep
%setup -q -a1 -a2 -a3
%patch0 -p1
%patch1 -p1

for dir in *-%{version}; do
	[ -f $dir/ChangeLog ] && mv $dir/ChangeLog ChangeLog-$dir
	rm -rf $dir/git-hooks
	mv $dir/* .
done

install -d ext_sources
ln %{SOURCE20} ext_sources
ln %{SOURCE21} ext_sources
ln %{SOURCE22} ext_sources
ln %{SOURCE23} ext_sources
ln %{SOURCE24} ext_sources
ln %{SOURCE25} ext_sources
ln %{SOURCE26} ext_sources
ln %{SOURCE27} ext_sources
:> src.downloaded

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -f /proc/cpuinfo ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

# Skip optimization. It overwrites some OOo own hacks with -O0
SAFE_CFLAGS=""
for i in %{rpmcflags}; do
	case "$i" in
	-O?|-pipe|-Wall|-g|-fexceptions|-fomit-frame-pointer)
		;;
	*)
		SAFE_CFLAGS="$SAFE_CFLAGS $i"
		;;
	esac
done

export CC="%{__cc}"
export CXX="%{__cxx}"
export CPP="%{__cpp}"

export IGNORE_MANIFEST_CHANGES=1
export QT4INC="%{_includedir}/qt4"
export QT4LIB="%{_libdir}"
export QT4DIR="%{_libdir}/qt4"

%if %{with java}
export JAVA_HOME="%{java_home}"
export DB_JAR="%{_javadir}/db.jar"
export ANT_HOME="%{_datadir}/ant"
%endif

%if %{with ccache}
if [ "$CCACHE_DIR" = "" ] ; then
	export CCACHE_DIR=$HOME/.ccache/
fi
%endif

%if %{with parallelbuild}
RPM_BUILD_NR_THREADS=$(echo %{_smp_mflags} | cut -dj -f2)
[ -z "$RPM_BUILD_NR_THREADS" ] && RPM_BUILD_NR_THREADS=1
%else
RPM_BUILD_NR_THREADS="1"
%endif

%{__aclocal} -I m4
%{__autoconf}
touch autogen.lastrun

# get automatic backtraces while building (required gdb, too)
ulimit -c unlimited || :

export PATH=$PATH:%{_libdir}/interbase/bin
%configure \
	--with-vendor="%{distribution}" \
	--with-extra-buildid="%{name}-%{epoch}:%{version}-%{release}" \
	--enable-release-build \
	--with-parallelism=$RPM_BUILD_NR_THREADS \
	--disable-odk \
	--with-system-libs \
	%{?with_ccache:--with-gcc-speedup=ccache} \
	%{!?with_system_coinmp:--without-system-coinmp} \
	%{?with_icecream:--with-gcc-speedup=icecream} \
	%{?with_system_agg:--with-system-agg} \
	%{?with_system_beanshell:--with-system-beanshell} \
	--with%{!?with_system_hsqldb:out}-system-hsqldb \
	%{?with_system_hunspell:--with-system-hunspell --without-myspell-dicts} \
	%{?with_system_libhnj:--with-system-altlinuxhyphen} \
	%{?with_msaccess:--with%{!?with_system_mdbtools:out}-system-mdbtools}} \
	--enable-python=system \
        --with-external-dict-dir=%{_datadir}/myspell \
	--with-external-tar=$(pwd)/ext_sources \
	--with-junit=%{_javadir}/junit.jar \
	--enable-ext-nlpsolver \
	--enable-pdfimport \
	--enable-ext-wiki-publisher \
	--enable-report-builder \
	--enable-scripting-beanshell \
	--enable-scripting-javascript \
	--%{?with_kde4:en}%{!?with_kde4:dis}able-kde4 \
	--with-lang=%{?with_i18n:ALL} \
%if %{with java}
	--with-java \
	--with-jdk-home=$JAVA_HOME \
	--with-ant-home=$ANT_HOME \
%else
	--without-java \
%endif
	--enable-gio \
	--with-x \
	--without-fonts \
	--disable-epm \
	--%{?with_gtk:en}%{!?with_gtk:dis}able-gtk \
	--%{?with_gtk3:en}%{!?with_gtk3:dis}able-gtk3 \
	--enable-dbus \
	--with-system-openldap \
%if 0%{?debug:1}
	--enable-debug \
	--enable-breakpad=yes \
	--enable-symbols=FULL \
%else
	--enable-breakpad=no \
	--disable-symbols \
%endif
	--with-build-version=%{version}-%{release} \
	--enable-split-app-modules \
	--enable-split-opt-features \
	--enable-cups \
	--disable-fetch-external

# this limits processing some files but doesn't limit parallel build
# processes of main OOo build (since OOo uses it's own build system)
export ARCH_FLAGS="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CC="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CXX="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden"
export ARCH_FLAGS_OPT="$SAFE_CFLAGS"

%{__make} -j1 verbose=true build-nocheck

%if %{with tests}
%{__make} -j1 verbose=true check
%endif

%install
rm -rf $RPM_BUILD_ROOT
# install just once (based on makeinstall.stamp)
# this will make packaging newer versions simplier
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	%{__rm} -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	export QTINC="%{_includedir}/qt"
	export QTLIB="%{_libdir}"
	export QT4DIR="%{_libdir}/qt4"
	export DESTDIR=$RPM_BUILD_ROOT
	export TMP="%{tmpdir}"
	export TMPDIR="%{tmpdir}"
	export TEMP="%{tmpdir}"
	export DEFAULT_TO_ENGLISH_FOR_PACKING=1

	%{__make} distro-pack-install \
		DESTDIR=$RPM_BUILD_ROOT

	# save orignal install layout
	find $RPM_BUILD_ROOT -ls > ls.txt
	touch makeinstall.stamp
fi

# mangle files installed in build root
if [ ! -f installed.stamp ]; then
	chmod -Rf a+rX,u+w,g-w,o-w $RPM_BUILD_ROOT

	%if %{with mono}
	%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/mono-ooo-2.1.pc
	%endif

	%if %{with mozilla}
	install -d $RPM_BUILD_ROOT%{_browserpluginsdir}
	ln -s %{_libdir}/%{name}/program/libnpsoplugin.so $RPM_BUILD_ROOT%{_browserpluginsdir}
	%endif

	perl -pi -e 's/^[       ]*LD_LIBRARY_PATH/# LD_LIBRARY_PATH/;s/export LD_LIBRARY_PATH/# export LD_LIBRARY_PATH/' \
		$RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup

	chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.so

	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/program
	# put share to %{_datadir} so we're able to produce noarch packages
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/help $RPM_BUILD_ROOT/%{_datadir}/%{name}
	ln -s ../../share/%{name}/help $RPM_BUILD_ROOT%{_libdir}/%{name}/help
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/readmes $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/share $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/share $RPM_BUILD_ROOT%{_libdir}/%{name}/share
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/program/resource $RPM_BUILD_ROOT%{_datadir}/%{name}/program
	ln -s ../../../share/%{name}/program/resource $RPM_BUILD_ROOT%{_libdir}/%{name}/program/resource

	%{__rm} -r $RPM_BUILD_ROOT%{_desktopdir}/*.desktop \
		$RPM_BUILD_ROOT%{_iconsdir}/{gnome,locolor} \
		$RPM_BUILD_ROOT%{_datadir}/application-registry
	for a in $RPM_BUILD_ROOT%{_datadir}/%{name}/share/xdg/*.desktop; do
		cp $a $RPM_BUILD_ROOT%{_desktopdir}/libreoffice-$(basename "$a")
	done
	%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/share/xdg

	# Make oo* -> lo* symlinks for compatibility with misc software,
	# for example mailcap
	ln -s libreoffice $RPM_BUILD_ROOT%{_bindir}/ooffice
	for a in fromtemplate base calc draw writer impress math web; do
		ln -s lo$a $RPM_BUILD_ROOT%{_bindir}/oo$a
	done

	%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/share/extensions/nlpsolver/help/*.done
	%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/share/extensions/wiki-publisher/help/*.done
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/program/classes/smoketest.jar

	touch installed.stamp
fi

# Find out locales
find_lang() {
	local lang=$(echo $1 | sed -e 's/_/-/')
	local langfn="$1"
	echo "%%defattr(644,root,root,755)" > ${langfn}.lang

	# help files
	if [ -f file-lists/help_${langfn}_list.txt ]; then
		cat file-lists/help_${langfn}_list.txt >> ${langfn}.lang
	fi

	lfile="file-lists/lang_${langfn}_list.txt"
	if [ -f ${lfile} ]; then
		lprefix=$(bin/openoffice-xlate-lang -p ${lang} 2>/dev/null || :)
		longlang=$(bin/openoffice-xlate-lang -l ${lang} 2>/dev/null || :)
		# share/*/${longlang}
		if [ "x${longlang}" != "x" ] ; then
			grep "^%%dir.*/${longlang}/\$" ${lfile} > tmp.lang || :
		fi
		# share/registry/res/${lang} (but en-US for en)
		grep "^%%dir.*/res/${lang}[^/]*/\$" ${lfile} >> tmp.lang || :
		# ... translate %dir into whole tree, handle special wordbook/english case
		sed -e 's,^%%dir ,,;s,\(wordbook/english/\)$,\1soffice.dic,;s,/$,,' tmp.lang >> ${langfn}.lang || :
		# share/autocorr/acor${somecodes}.dat (if exist)
		grep '/autocorr/acor.*dat$' ${lfile} >> ${langfn}.lang || :
		# user/config/* (if exist, without parent directory)
		grep '/user/config/..*' ${lfile} >> ${langfn}.lang || :
		grep "/licenses/LICENSE_${lang}" ${lfile} >> ${langfn}.lang || :
		grep "/readmes/README_${lang}" ${lfile} >> ${langfn}.lang || :
		grep "share/readme/LICENSE_${lang}" ${lfile} >> ${langfn}.lang || :
		grep "share/readme/README_${lang}" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/presers/config/*.so[cdegh]
		grep "/presets/config/.*_${lang}\.so[cdegh]$" ${lfile} >> ${langfn}.lang || :
		if [ "x${lprefix}" != "x" ] ; then
			grep "/presets/config/${lprefix}.*\.so[cdegh]$" ${lfile} >> ${langfn}.lang || :
		fi
		# lib/openoffice.org/program/resource/*.res
		grep "/program/resource/.*${lang}.res$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/autocorr/*.dat
		grep "/share/autocorr/.*${lang}.dat$" ${lfile} >> ${langfn}.lang || :
		grep -i "/share/autocorr/.*${lang}-${lang}.dat$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/autotext/$lang
		grep "/share/autotext/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/autotext/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_datadir}/%{name}/share/registry/.*[_-]$lang.xcd
		grep "/share/registry/.*[_-]${lang}.xcd$" ${lfile} >> ${langfn}.lang || :
		# %{_datadir}/%{name}/share/template/$lang
		grep "/share/template/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_datadir}/%{name}/share/template/wizard/letter/lang
		grep "/share/template/wizard/letter/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}$" file-lists/common_list.txt >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" file-lists/common_list.txt >> ${langfn}.lang || :
		# %{_datadir}/%{name}/share/wordbook/$lang
		grep "/share/wordbook/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/wordbook/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_datadir}/%{name}/share/samples/$lang
		grep "/share/samples/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/samples/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_libdir}/%{name}/help/$lang
		grep "/help/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/help/${lang}/" ${lfile} >> ${langfn}.lang || :
		# UI translations
		grep "/soffice.cfg/[^/]*/ui/res/${lang}.zip" ${lfile} >> ${langfn}.lang || :
		grep "/soffice.cfg/modules/[^/]*/ui/res/${lang}.zip" ${lfile} >> ${langfn}.lang || :
		# Translations
		if [ -d "$RPM_BUILD_ROOT%{_datadir}/%{name}/program/resource/${langfn}" ]; then
			echo "%lang(${langfn}) %{_datadir}/%{name}/program/resource/${langfn}" >> ${langfn}.lang
		fi
		if [ -f "$RPM_BUILD_ROOT%{_datadir}/%{name}/share/wizards/resources_${langfn}.properties" ]; then
			echo "%lang(${langfn}) %{_datadir}/%{name}/share/wizards/resources_${langfn}.properties" >> ${langfn}.lang
		fi

		for e in wiki-publisher nlpsolver ; do
			for f in $RPM_BUILD_ROOT%{_datadir}/%{name}/share/extensions/$e/description-${lang}.txt \
					$RPM_BUILD_ROOT%{_datadir}/%{name}/share/extensions/$e/locale/*_${langfn}.properties \
					$RPM_BUILD_ROOT%{_datadir}/%{name}/share/extensions/$e/help/${lang} ; do
				[ -e $f ] && echo "%lang(${langfn}) $f" | sed -e "s|$RPM_BUILD_ROOT||g" >> $e.lang || :
			done
		done
	fi
}

%if %{with i18n}
%{__rm} -f *.lang*
langlist=$(ls file-lists/lang_*_list.txt | sed -e 's=file-lists/lang_\(.*\)_list.txt=\1=g')

for lang in $langlist; do
	find_lang $lang
done

%{__sed} -i -e '
	s,%{_libdir}/%{name}/share,%{_datadir}/%{name}/share,;
	s,%{_libdir}/%{name}/readmes,%{_datadir}/%{name}/readmes,;
	s,%{_libdir}/%{name}/help,%{_datadir}/%{name}/help,;
	s,%{_libdir}/%{name}/program/resource,%{_datadir}/%{name}/program/resource,;
' *.lang
%endif

# Fix incorrect file list, help files listed but not installed
for l in lb bn_IN; do
	%{__sed} -i -e '/.*\/help\/.*/d' $l.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans core
if [ -d %{_libdir}/%{name}/program/resource ] && [ ! -L %{_libdir}/%{name}/program/resource ]; then
	install -d %{_datadir}/%{name}/program
	if [ -e %{_datadir}/%{name}/program/resource ]; then
		%{__mv} %{_datadir}/%{name}/program/resource{,.rpmsave}
	fi
	%{__mv} -v %{_libdir}/%{name}/program/resource %{_datadir}/%{name}/program/resource
	ln -s %{_datadir}/%{name}/program/resource %{_libdir}/%{name}/program/resource
fi
if [ -d %{_libdir}/%{name}/share ] && [ ! -L %{_libdir}/%{name}/share ]; then
	install -d %{_datadir}/%{name}
	if [ -e %{_datadir}/%{name}/share ]; then
		%{__mv} %{_datadir}/%{name}/share{,.rpmsave}
	fi
	%{__mv} -v %{_libdir}/%{name}/share %{_datadir}/%{name}/share
	ln -s %{_datadir}/%{name}/share %{_libdir}/%{name}/share
fi
exit 0

%post core
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun core
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%post base
%update_desktop_database_post
%update_icon_cache hicolor

%postun base
%update_desktop_database_postun
%update_icon_cache hicolor

%post web
%update_desktop_database_post

%postun web
%update_desktop_database_postun

%post writer
%update_desktop_database_post
%update_icon_cache hicolor

%postun writer
%update_desktop_database_postun
%update_icon_cache hicolor

%post calc
%update_desktop_database_post
%update_icon_cache hicolor

%postun calc
%update_desktop_database_postun
%update_icon_cache hicolor

%post draw
%update_desktop_database_post
%update_icon_cache hicolor

%postun draw
%update_desktop_database_postun
%update_icon_cache hicolor

%post impress
%update_desktop_database_post
%update_icon_cache hicolor

%postun impress
%update_desktop_database_postun
%update_icon_cache hicolor

%post math
%update_desktop_database_post
%update_icon_cache hicolor

%postun math
%update_desktop_database_postun
%update_icon_cache hicolor

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

# NOTE:
# you may find file-lists/*_list.txt useful to help you package files to packages

%files
%defattr(644,root,root,755)

%files core
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/CREDITS*
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/NOTICE

%attr(755,root,root) %{_bindir}/libreoffice
%attr(755,root,root) %{_bindir}/lofromtemplate
%attr(755,root,root) %{_bindir}/loffice
%attr(755,root,root) %{_bindir}/ooffice
%attr(755,root,root) %{_bindir}/oofromtemplate
%attr(755,root,root) %{_bindir}/soffice
%attr(755,root,root) %{_bindir}/unopkg

%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/help
%{_datadir}/%{name}/help/*.xsl

%dir %{_libdir}/%{name}/presets
%dir %{_libdir}/%{name}/presets/autotext
%{_libdir}/%{name}/presets/autotext/mytexts.bau
%{_libdir}/%{name}/presets/basic
%dir %{_libdir}/%{name}/presets/config
%{_libdir}/%{name}/presets/config/autotbl.fmt
%{_libdir}/%{name}/presets/database
%{_libdir}/%{name}/presets/gallery

%dir %{_libdir}/%{name}/program
%attr(755,root,root) %{_libdir}/%{name}/program/gdbtrace
%attr(755,root,root) %{_libdir}/%{name}/program/gengal
%attr(755,root,root) %{_libdir}/%{name}/program/gengal.bin
%attr(755,root,root) %{_libdir}/%{name}/program/java-set-classpath
%attr(755,root,root) %{_libdir}/%{name}/program/libCbc.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libCbcSolver.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libCgl.so.1
%attr(755,root,root) %{_libdir}/%{name}/program/libClp.so.1
%attr(755,root,root) %{_libdir}/%{name}/program/libCoinMP.so.1
%attr(755,root,root) %{_libdir}/%{name}/program/libCoinUtils.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libOsi.so.1
%attr(755,root,root) %{_libdir}/%{name}/program/libOsiClp.so.1
%attr(755,root,root) %{_libdir}/%{name}/program/libacclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmediagst*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmedialo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasctllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasegfxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasprovlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbiblo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcached1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcairocanvaslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcanvasfactorylo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcanvastoolslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartcontrollerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartcorelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartopengllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcmdmaillo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcollator_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcomphelper.so
%attr(755,root,root) %{_libdir}/%{name}/program/libconfigmgrlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcppcanvaslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libctllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcuilo.so
%{!?with_system_db:%attr(755,root,root) %{_libdir}/%{name}/program/libdb-4.2.so}
%attr(755,root,root) %{_libdir}/%{name}/program/libdbalo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbaselo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbaxmllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbmmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbpool2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbtoolslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbulo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeployment.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeploymentgui.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeploymentmisclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdesktop_detectorlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdesktopbe1lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdict_ja.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdict_zh.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdlgprovlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdrawinglayerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeditenglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libembobj.so
%attr(755,root,root) %{_libdir}/%{name}/program/libemboleobj.so
%attr(755,root,root) %{_libdir}/%{name}/program/libemfiolo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libevtattlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libexpwraplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfilelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfilterconfiglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfirebird_sdbclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libflatlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libforlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libforuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfps_officelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfrmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfsstoragelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libgielo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libguesslanglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libhelplinkerlo.so
%{!?with_system_hunspell:%attr(755,root,root) %{_libdir}/%{name}/program/libhunspell.so}
%attr(755,root,root) %{_libdir}/%{name}/program/libhyphenlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nlangtag.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18npoollo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nsearchlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nutil.so
%attr(755,root,root) %{_libdir}/%{name}/program/libicglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libindex_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libldapbe2lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblnglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblnthlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocalebe1lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_en.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_es.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_euro.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_others.so
%attr(755,root,root) %{_libdir}/%{name}/program/libloglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblosessioninstalllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmcnttype.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmigrationoo2lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmigrationoo3lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmorklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmozbootstraplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmsfilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmsformslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmtfrendererlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmysqllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodfflatxmllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liboffacclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liboglcanvaslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libooxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpackage2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpasswordcontainerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpcrlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpdffilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpdfiumlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpricinglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libprotocolhandlerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librecentfile.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsaxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsblo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscnlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscriptframe.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbtlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsddlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdfiltlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsduilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsfxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsimplecanvaslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libslideshowlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsofficeapp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsotlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspelllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsrtrs1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libstoragefdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libstringresourcelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvgiolo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvtlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvxcorelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsysshlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconv_dict.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconversiondlgslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextfdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucb1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucbhelper.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpchelp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpcmis1lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpdav1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpexpand1lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpextlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpfile1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpftp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpgio1lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucphier1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpimagelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucppkg1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucptdoc1lo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunopkgapp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunordflo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunoxmllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libupdatefeedlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libutllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvbaeventslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvbahelperlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclcanvaslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvcllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_genlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpftdrawlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwriterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwriterperfectlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlfalo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlfdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlscriptlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlsecurity.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxoflo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxolo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsec_fw.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsec_xmlsec.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsltdlglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsltfilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxstor.so
%attr(755,root,root) %{_libdir}/%{name}/program/oosplash
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
%attr(755,root,root) %{_libdir}/%{name}/program/senddoc
%attr(755,root,root) %{_libdir}/%{name}/program/uri-encode
%attr(755,root,root) %{_libdir}/%{name}/program/xid-fullscreen-on-all-monitors

%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/libhsqldb.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjdbclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libofficebean.so
%endif

%if %{with mono}
%attr(755,root,root) %{_libdir}/%{name}/program/libcli_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcli_uno_glue.so
%{_libdir}/%{name}/program/cli_basetypes.dll
%{_libdir}/%{name}/program/cli_cppuhelper.dll
%{_libdir}/%{name}/program/cli_types.dll
%{_libdir}/%{name}/program/cli_uno_bridge.dll
%{_libdir}/%{name}/program/cli_ure.dll
%endif

%config(noreplace) %verify(not md5 mtime size) %{_libdir}/%{name}/program/lounorc
%{_libdir}/%{name}/program/versionrc

%{_libdir}/%{name}/program/intro-highres.png

%{_libdir}/%{name}/program/services.rdb
%dir %{_libdir}/%{name}/program/services
%{_libdir}/%{name}/program/services/services.rdb

%if %{with java}
%dir %{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/program/classes/reportbuilder.jar
%{_libdir}/%{name}/program/classes/reportbuilderwizard.jar
%{_libdir}/%{name}/program/classes/ScriptFramework.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForBeanShell.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForJavaScript.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForJava.jar
%{_libdir}/%{name}/program/classes/XMergeBridge.jar
%{_libdir}/%{name}/program/classes/commonwizards.jar
%{_libdir}/%{name}/program/classes/form.jar
%{!?with_system_hsqldb:%{_libdir}/%{name}/program/classes/hsqldb.jar}
%{_libdir}/%{name}/program/classes/js.jar
%{_libdir}/%{name}/program/classes/officebean.jar
%{_libdir}/%{name}/program/classes/query.jar
%{_libdir}/%{name}/program/classes/report.jar
%{_libdir}/%{name}/program/classes/sdbc_hsqldb.jar
%{!?with_system_xalan:%{_libdir}/%{name}/program/classes/serializer.jar}
%{_libdir}/%{name}/program/classes/table.jar
%{_libdir}/%{name}/program/classes/unoil.jar
%{!?with_system_xalan:%{_libdir}/%{name}/program/classes/xalan.jar}
%{_libdir}/%{name}/program/classes/xmerge.jar
%{_libdir}/%{name}/program/services/scriptproviderforbeanshell.rdb
%{_libdir}/%{name}/program/services/scriptproviderforjavascript.rdb
%endif
%dir %{_libdir}/%{name}/program/types
%{_libdir}/%{name}/program/types/offapi.rdb
%{_libdir}/%{name}/program/types/oovbaapi.rdb

%dir %{_libdir}/%{name}/program/opencl
%{_libdir}/%{name}/program/opencl/cl-test.ods
%dir %{_libdir}/%{name}/program/opengl
%{_libdir}/%{name}/program/opengl/areaHashCRC64TFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/areaScaleFastFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/areaScaleFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/backgroundFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/backgroundVertexShader.glsl
%{_libdir}/%{name}/program/opengl/basicFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/basicVertexShader.glsl
%{_libdir}/%{name}/program/opengl/blendedTextureFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/blendedTextureVertexShader.glsl
%{_libdir}/%{name}/program/opengl/combinedFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/combinedTextureFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/combinedTextureVertexShader.glsl
%{_libdir}/%{name}/program/opengl/combinedVertexShader.glsl
%{_libdir}/%{name}/program/opengl/commonFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/commonVertexShader.glsl
%{_libdir}/%{name}/program/opengl/convolutionFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/debugFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/debugVertexShader.glsl
%{_libdir}/%{name}/program/opengl/diffTextureFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/dissolveFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/dumbVertexShader.glsl
%{_libdir}/%{name}/program/opengl/dummyVertexShader.glsl
%{_libdir}/%{name}/program/opengl/fadeBlackFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/fadeFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/glitterFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/glitterVertexShader.glsl
%{_libdir}/%{name}/program/opengl/greyscaleFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/honeycombFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/honeycombGeometryShader.glsl
%{_libdir}/%{name}/program/opengl/honeycombVertexShader.glsl
%{_libdir}/%{name}/program/opengl/invert50FragmentShader.glsl
%{_libdir}/%{name}/program/opengl/linearGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/linearMultiColorGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/linearTwoColorGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/lineFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/lineVertexShader.glsl
%{_libdir}/%{name}/program/opengl/maskedTextureFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/maskedTextureVertexShader.glsl
%{_libdir}/%{name}/program/opengl/maskFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/pickingFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/pickingVertexShader.glsl
%{_libdir}/%{name}/program/opengl/radialGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/radialMultiColorGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/radialTwoColorGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/rectangularMultiColorGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/rectangularTwoColorGradientFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/reflectionFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/reflectionVertexShader.glsl
%{_libdir}/%{name}/program/opengl/renderTextureFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/renderTextureVertexShader.glsl
%{_libdir}/%{name}/program/opengl/replaceColorFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/rippleFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/screenTextFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/screenTextVertexShader.glsl
%{_libdir}/%{name}/program/opengl/shape3DFragmentShaderBatch.glsl
%{_libdir}/%{name}/program/opengl/shape3DFragmentShaderBatchScroll.glsl
%{_libdir}/%{name}/program/opengl/shape3DFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/shape3DFragmentShaderV300.glsl
%{_libdir}/%{name}/program/opengl/shape3DVertexShaderBatch.glsl
%{_libdir}/%{name}/program/opengl/shape3DVertexShaderBatchScroll.glsl
%{_libdir}/%{name}/program/opengl/shape3DVertexShader.glsl
%{_libdir}/%{name}/program/opengl/shape3DVertexShaderV300.glsl
%{_libdir}/%{name}/program/opengl/solidFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/staticFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/symbolFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/symbolVertexShader.glsl
%{_libdir}/%{name}/program/opengl/textFragmentShaderBatch.glsl
%{_libdir}/%{name}/program/opengl/textFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/textureFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/textureVertexShader.glsl
%{_libdir}/%{name}/program/opengl/textVertexShaderBatch.glsl
%{_libdir}/%{name}/program/opengl/textVertexShader.glsl
%{_libdir}/%{name}/program/opengl/transformedTextureVertexShader.glsl
%{_libdir}/%{name}/program/opengl/vortexFragmentShader.glsl
%{_libdir}/%{name}/program/opengl/vortexGeometryShader.glsl
%{_libdir}/%{name}/program/opengl/vortexVertexShader.glsl

# symlink
%{_libdir}/%{name}/program/resource
%dir %{_datadir}/%{name}/program
%dir %{_datadir}/%{name}/program/resource

%dir %{_datadir}/%{name}/share
%dir %{_datadir}/%{name}/share/labels
%{_datadir}/%{name}/share/labels/labels.xml
%dir %{_datadir}/%{name}/share/Scripts
%{_datadir}/%{name}/share/Scripts/beanshell
%{_datadir}/%{name}/share/Scripts/javascript
%if %{with java}
%{_datadir}/%{name}/share/Scripts/java
%endif

%dir %{_datadir}/%{name}/share/autocorr
%{_datadir}/%{name}/share/autocorr/acor_*.dat
%dir %{_datadir}/%{name}/share/autotext
%{_datadir}/%{name}/share/autotext/en-US
%{_datadir}/%{name}/share/basic
%{_datadir}/%{name}/share/classification
%dir %{_datadir}/%{name}/share/config
%{_datadir}/%{name}/share/config/images_breeze.zip
%{_datadir}/%{name}/share/config/images_breeze_dark.zip
%{_datadir}/%{name}/share/config/images_elementary.zip
%{_datadir}/%{name}/share/config/images_galaxy.zip
%{_datadir}/%{name}/share/config/images_hicontrast.zip
%{_datadir}/%{name}/share/config/images_sifr.zip
%{_datadir}/%{name}/share/config/images_sifr_dark.zip
%{_datadir}/%{name}/share/config/images_tango.zip
%dir %{_datadir}/%{name}/share/config/soffice.cfg
%dir %{_datadir}/%{name}/share/config/soffice.cfg/cui
%{_datadir}/%{name}/share/config/soffice.cfg/cui/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/dbaccess
%{_datadir}/%{name}/share/config/soffice.cfg/dbaccess/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/desktop
%{_datadir}/%{name}/share/config/soffice.cfg/desktop/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/editeng
%{_datadir}/%{name}/share/config/soffice.cfg/editeng/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/filter
%{_datadir}/%{name}/share/config/soffice.cfg/filter/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/formula/
%{_datadir}/%{name}/share/config/soffice.cfg/formula/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/fps
%{_datadir}/%{name}/share/config/soffice.cfg/fps/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules
%{_datadir}/%{name}/share/config/soffice.cfg/modules/BasicIDE
%{_datadir}/%{name}/share/config/soffice.cfg/modules/StartModule
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/dbapp
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/dbbrowser
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/dbquery
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/dbtdata
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sabpilot
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/scanner
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scanner/ui
%{_datadir}/%{name}/share/config/soffice.cfg/modules/schart
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/sglobal
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sglobal/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sglobal/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sglobal/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sglobal/toolbar
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/smath
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/sweb
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress
%{_datadir}/%{name}/share/config/soffice.cfg/modules/spropctrlr
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swform
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/toolbar
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/toolbar
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/toolbar
%dir %{_datadir}/%{name}/share/config/soffice.cfg/sfx
%{_datadir}/%{name}/share/config/soffice.cfg/sfx/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/svt
%{_datadir}/%{name}/share/config/soffice.cfg/svt/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/svx
%{_datadir}/%{name}/share/config/soffice.cfg/svx/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/uui
%{_datadir}/%{name}/share/config/soffice.cfg/uui/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/vcl
%{_datadir}/%{name}/share/config/soffice.cfg/vcl/ui
%dir %{_datadir}/%{name}/share/config/soffice.cfg/xmlsec
%{_datadir}/%{name}/share/config/soffice.cfg/xmlsec/ui
%{_datadir}/%{name}/share/config/webcast
%{_datadir}/%{name}/share/config/wizard
%dir %{_datadir}/%{name}/share/dtd
%{_datadir}/%{name}/share/dtd/officedocument
%{_datadir}/%{name}/share/emojiconfig
%dir %{_datadir}/%{name}/share/extensions
%{_datadir}/%{name}/share/extensions/package.txt
%{_datadir}/%{name}/share/filter
%{_datadir}/%{name}/share/fonts
%{_datadir}/%{name}/share/gallery
%{_datadir}/%{name}/share/palette
%{_datadir}/%{name}/share/psprint

%dir %{_datadir}/%{name}/share/registry
%{_datadir}/%{name}/share/registry/reportbuilder.xcd
%{_datadir}/%{name}/share/registry/Langpack-en-US.xcd
%{_datadir}/%{name}/share/registry/lingucomponent.xcd
%{_datadir}/%{name}/share/registry/main.xcd
%{_datadir}/%{name}/share/registry/oo-ad-ldap.xcd.sample
%{_datadir}/%{name}/share/registry/oo-ldap.xcd.sample
%dir %{_datadir}/%{name}/share/registry/res
%{_datadir}/%{name}/share/registry/res/fcfg_langpack_en-US.xcd

%dir %{_datadir}/%{name}/share/template
%dir %{_datadir}/%{name}/share/template/common
%{_datadir}/%{name}/share/template/common/internal
%{_datadir}/%{name}/share/template/common/officorr
%{_datadir}/%{name}/share/template/common/offimisc
%{_datadir}/%{name}/share/template/common/personal
%{_datadir}/%{name}/share/template/common/presnt
%{_datadir}/%{name}/share/template/common/styles
%dir %{_datadir}/%{name}/share/template/wizard
%{_datadir}/%{name}/share/template/wizard/bitmap
%dir %{_datadir}/%{name}/share/template/common/wizard
%{_datadir}/%{name}/share/template/common/wizard/agenda
%{_datadir}/%{name}/share/template/common/wizard/fax
%{_datadir}/%{name}/share/template/common/wizard/letter
%{_datadir}/%{name}/share/template/common/wizard/report
%{_datadir}/%{name}/share/template/common/wizard/styles

%dir %{_datadir}/%{name}/share/wizards

%dir %{_datadir}/%{name}/share/wordbook
%{_datadir}/%{name}/share/wordbook/en-GB.dic
%{_datadir}/%{name}/share/wordbook/en-US.dic
%{_datadir}/%{name}/share/wordbook/sl.dic
%{_datadir}/%{name}/share/wordbook/technical.dic

%dir %{_datadir}/%{name}/share/xslt
%{_datadir}/%{name}/share/xslt/common
%dir %{_datadir}/%{name}/share/xslt/export
%{_datadir}/%{name}/share/xslt/export/common
%{_datadir}/%{name}/share/xslt/export/spreadsheetml
%{_datadir}/%{name}/share/xslt/export/uof
%{_datadir}/%{name}/share/xslt/export/wordml
%{_datadir}/%{name}/share/xslt/import

%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/soffice.bin
%attr(755,root,root) %{_libdir}/%{name}/program/unoinfo
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg.bin
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/flat_logo.svg
%{_libdir}/%{name}/program/fundamentalrc
%{_libdir}/%{name}/program/intro.png
%{_libdir}/%{name}/program/redirectrc
%{_libdir}/%{name}/program/setuprc
%{_libdir}/%{name}/program/shell
%{_libdir}/%{name}/program/sofficerc

# symlinks
%{_libdir}/%{name}/help
%{_libdir}/%{name}/readmes
%{_libdir}/%{name}/share

%dir %{_datadir}/%{name}/readmes
%{_datadir}/%{name}/readmes/README_en-US

%{_datadir}/mime/packages/libreoffice.xml
%{_iconsdir}/hicolor/*/mimetypes/libreoffice-*.png
%{_iconsdir}/hicolor/*/mimetypes/libreoffice-*.svg
%{_iconsdir}/hicolor/*/apps/libreoffice-main.png
%{_iconsdir}/hicolor/*/apps/libreoffice-main.svg

%{_desktopdir}/libreoffice-startcenter.desktop
%{_desktopdir}/libreoffice-qstart.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-startcenter.png
%{_iconsdir}/hicolor/*/apps/libreoffice-startcenter.svg

%{_mandir}/man1/loffice.1
%{_mandir}/man1/lofromtemplate.1
%{_mandir}/man1/libreoffice.1*
%{_mandir}/man1/unopkg.1*

%if %{with kde4}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde4*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libkde4be1lo.so
%endif

%if %{with gtk} || %{with gtk3}
%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libqstart_gtklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gtk*.so
%{_datadir}/%{name}/share/registry/gnome.xcd
%endif

%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lobase
%attr(755,root,root) %{_bindir}/oobase
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%{_mandir}/man1/lobase.1
%{_desktopdir}/libreoffice-base.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-base.png
%{_iconsdir}/hicolor/*/apps/libreoffice-base.svg
%attr(755,root,root) %{_libdir}/%{name}/program/libabplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptxmllo.so
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbapp/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbapp/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbapp/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbapp/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbbrowser/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbbrowser/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbbrowser/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbquery/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbquery/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbrelation
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport/ui
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbtable
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbtdata/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbtdata/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbtdata/toolbar
%{_datadir}/%{name}/share/registry/base.xcd
%{_datadir}/appdata/libreoffice-base.appdata.xml
%{_datadir}/appdata/org.libreoffice.kde.metainfo.xml

%files calc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/localc
%attr(755,root,root) %{_bindir}/oocalc
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%{_mandir}/man1/localc.1
%{_desktopdir}/libreoffice-calc.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-calc.png
%{_iconsdir}/hicolor/*/apps/libreoffice-calc.svg
%attr(755,root,root) %{_libdir}/%{name}/program/libanalysislo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcalclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libclewlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdatelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libopencllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscfiltlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsolverlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvbaobjlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpftcalclo.so
%{_datadir}/%{name}/share/calc
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc/ui
%{_datadir}/%{name}/share/registry/calc.xcd
%{_datadir}/appdata/libreoffice-calc.appdata.xml

%files draw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lodraw
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%{_mandir}/man1/lodraw.1
%{_desktopdir}/libreoffice-draw.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-draw.png
%{_iconsdir}/hicolor/*/apps/libreoffice-draw.svg
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw/ui
%{_datadir}/%{name}/share/registry/draw.xcd
%{_datadir}/appdata/libreoffice-draw.appdata.xml

%files emailmerge
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/mailmerge.py*
%{_libdir}/%{name}/program/msgbox.py*

%files writer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lowriter
%attr(755,root,root) %{_bindir}/oowriter
%attr(755,root,root) %{_libdir}/%{name}/program/libhwplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblwpftlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmswordlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libt602filterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpftwriterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwriterfilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvbaswobjlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%{_mandir}/man1/lowriter.1
%{_desktopdir}/libreoffice-writer.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-writer.png
%{_iconsdir}/hicolor/*/apps/libreoffice-writer.svg
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sbibliography
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter/ui
%{_datadir}/%{name}/share/config/soffice.cfg/writerperfect
%{_datadir}/%{name}/share/registry/writer.xcd
%{_datadir}/appdata/libreoffice-writer.appdata.xml

%files impress
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/loimpress
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%attr(755,root,root) %{_libdir}/%{name}/program/libOGLTranslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcorelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libPresentationMinimizerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libPresenterScreenlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpftimpresslo.so
%{_mandir}/man1/loimpress.1
%{_desktopdir}/libreoffice-impress.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-impress.png
%{_iconsdir}/hicolor/*/apps/libreoffice-impress.svg
%{_datadir}/%{name}/share/config/soffice.cfg/simpress
%{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress/ui
%{_datadir}/%{name}/share/registry/impress.xcd
%{_datadir}/%{name}/share/registry/ogltrans.xcd
%{_datadir}/appdata/libreoffice-impress.appdata.xml

%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lomath
%attr(755,root,root) %{_bindir}/oomath
%{_mandir}/man1/lomath.1
%{_desktopdir}/libreoffice-math.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-math.png
%{_iconsdir}/hicolor/*/apps/libreoffice-math.svg
%attr(755,root,root) %{_libdir}/%{name}/program/libsmdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%{_datadir}/%{name}/share/config/soffice.cfg/modules/smath/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/smath/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/smath/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/smath/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/smath/ui
%{_datadir}/%{name}/share/registry/math.xcd

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/loweb
%attr(755,root,root) %{_bindir}/ooweb
%{_mandir}/man1/loweb.1
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sweb/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sweb/popupmenu
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sweb/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sweb/toolbar

%files graphicfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libflashlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvgfilterlo.so
%{_datadir}/%{name}/share/registry/graphicfilter.xcd
%attr(755,root,root) %{_libdir}/%{name}/program/libgraphicfilterlo.so

%files xsltfilter
%defattr(644,root,root,755)
%{_datadir}/%{name}/share/registry/xsltfilter.xcd
%{_datadir}/%{name}/share/xslt/docbook
%{_datadir}/%{name}/share/xslt/export/xhtml
%{_desktopdir}/libreoffice-xsltfilter.desktop

%files postgresql
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/postgresql-sdbc.ini
%{_libdir}/%{name}/program/services/postgresql-sdbc.rdb
%{_datadir}/%{name}/share/registry/postgresql.xcd
%attr(755,root,root) %{_libdir}/%{name}/program/libpostgresql-sdbclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpostgresql-sdbc-impllo.so

%files ure
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/program/regmerge
%attr(755,root,root) %{_libdir}/%{name}/program/regview
%attr(755,root,root) %{_libdir}/%{name}/program/uno
%attr(755,root,root) %{_libdir}/%{name}/program/uno.bin
%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%endif
%dir %{_libdir}/%{name}/program
%attr(755,root,root) %{_libdir}/%{name}/program/libaffine_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbinaryurplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbootstraplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libgcc3_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libintrospectionlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libinvocadaptlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libinvocationlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libiolo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjvmaccesslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjvmfwklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblog_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libnamingservicelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libproxyfaclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libreflectionlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libreglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsal_textenclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libstocserviceslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libstorelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_cppuhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_cppu.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libunoidllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_purpenvhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_salhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_sal.so.3
%attr(755,root,root) %{_libdir}/%{name}/program/libunsafe_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuuresolverlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlreaderlo.so
%{_libdir}/%{name}/program/jvmfwk3rc
%{_libdir}/%{name}/program/unorc
%if %{with java}
%{_libdir}/%{name}/program/JREProperties.class
%attr(755,root,root) %{_libdir}/%{name}/program/libjavaloaderlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjava_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjavavmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjpipe.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjuh.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjuhx.so
%endif
%if %{with java}
%dir %{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/program/classes/java_uno.jar
%{_libdir}/%{name}/program/classes/juh.jar
%{_libdir}/%{name}/program/classes/jurt.jar
%{_libdir}/%{name}/program/classes/ridl.jar
%{_libdir}/%{name}/program/classes/unoloader.jar
%endif
%if %{with java}
%{_libdir}/%{name}/program/javavendors.xml
%endif
%{_libdir}/%{name}/program/types.rdb

%files pyuno
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libpyuno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pyuno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpythonloaderlo.so
%{_libdir}/%{name}/program/pythonloader.unorc
%{_libdir}/%{name}/program/officehelper.py
%{_libdir}/%{name}/program/pythonloader.py
%{_libdir}/%{name}/program/pythonscript.py
%{_libdir}/%{name}/program/uno.py
%{_libdir}/%{name}/program/unohelper.py
%{_libdir}/%{name}/program/services/pyuno.rdb
%{_libdir}/%{name}/program/services/scriptproviderforpython.rdb
%{_datadir}/%{name}/share/registry/librelogo.xcd
%{_datadir}/%{name}/share/registry/pyuno.xcd

# python wizards
%dir %{_libdir}/%{name}/program/wizards
%{_libdir}/%{name}/program/wizards/*.py
%dir %{_libdir}/%{name}/program/wizards/agenda
%{_libdir}/%{name}/program/wizards/agenda/*.py
%dir %{_libdir}/%{name}/program/wizards/common
%{_libdir}/%{name}/program/wizards/common/*.py
%{_libdir}/%{name}/program/wizards/common/strings.hrc
%dir %{_libdir}/%{name}/program/wizards/document
%{_libdir}/%{name}/program/wizards/document/*.py
%dir %{_libdir}/%{name}/program/wizards/fax
%{_libdir}/%{name}/program/wizards/fax/*.py
%dir %{_libdir}/%{name}/program/wizards/letter
%{_libdir}/%{name}/program/wizards/letter/*.py
%dir %{_libdir}/%{name}/program/wizards/text
%{_libdir}/%{name}/program/wizards/text/*.py
%dir %{_libdir}/%{name}/program/wizards/ui
%{_libdir}/%{name}/program/wizards/ui/*.py
%dir %{_libdir}/%{name}/program/wizards/ui/event
%{_libdir}/%{name}/program/wizards/ui/event/*.py

# samples there
%{_datadir}/%{name}/share/Scripts/python

%files pdfimport
%defattr(644,root,root,755)
# -f pdfimport.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/xpdfimport
%{_datadir}/%{name}/share/registry/pdfimport.xcd
%{_datadir}/%{name}/share/xpdfimport
%attr(755,root,root) %{_libdir}/%{name}/program/libpdfimportlo.so

%files wiki-publisher -f wiki-publisher.lang
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/share/extensions/wiki-publisher
%{_datadir}/%{name}/share/extensions/wiki-publisher/META-INF
%{_datadir}/%{name}/share/extensions/wiki-publisher/WikiEditor
%{_datadir}/%{name}/share/extensions/wiki-publisher/filter
%dir %{_datadir}/%{name}/share/extensions/wiki-publisher/help
%{_datadir}/%{name}/share/extensions/wiki-publisher/license
%{_datadir}/%{name}/share/extensions/wiki-publisher/registration
%{_datadir}/%{name}/share/extensions/wiki-publisher/templates
%{_datadir}/%{name}/share/extensions/wiki-publisher/*.xc*
%{_datadir}/%{name}/share/extensions/wiki-publisher/components.rdb
%{_datadir}/%{name}/share/extensions/wiki-publisher/description.xml
%{_datadir}/%{name}/share/extensions/wiki-publisher/mediawiki.jar

%files nlpsolver -f nlpsolver.lang
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/share/extensions/nlpsolver
%{_datadir}/%{name}/share/extensions/nlpsolver/META-INF
%dir %{_datadir}/%{name}/share/extensions/nlpsolver/help
%dir %{_datadir}/%{name}/share/extensions/nlpsolver/locale
%{_datadir}/%{name}/share/extensions/nlpsolver/locale/*_en_US.default
%{_datadir}/%{name}/share/extensions/nlpsolver/registration
%{_datadir}/%{name}/share/extensions/nlpsolver/EvolutionarySolver.jar
%{_datadir}/%{name}/share/extensions/nlpsolver/components.rdb
%{_datadir}/%{name}/share/extensions/nlpsolver/description.xml
%{_datadir}/%{name}/share/extensions/nlpsolver/nlpsolver.jar

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libnpsoplugin.so
%endif

%if %{with i18n}
%files i18n-af -f af.lang
%defattr(644,root,root,755)

%files i18n-am -f am.lang
%defattr(644,root,root,755)

%files i18n-ar -f ar.lang
%defattr(644,root,root,755)

%files i18n-as -f as.lang
%defattr(644,root,root,755)

%files i18n-ast -f ast.lang
%defattr(644,root,root,755)

%files i18n-be_BY -f be.lang
%defattr(644,root,root,755)

%files i18n-bg -f bg.lang
%defattr(644,root,root,755)

%files i18n-bn -f bn.lang
%defattr(644,root,root,755)

%files i18n-bn_IN -f bn_IN.lang
%defattr(644,root,root,755)

%files i18n-bo -f bo.lang
%defattr(644,root,root,755)

%files i18n-br -f br.lang
%defattr(644,root,root,755)

%files i18n-brx -f brx.lang
%defattr(644,root,root,755)

%files i18n-bs -f bs.lang
%defattr(644,root,root,755)

%files i18n-ca -f ca.lang
%defattr(644,root,root,755)

%files i18n-ca_XV -f ca_valencia.lang
%defattr(644,root,root,755)

%files i18n-cs -f cs.lang
%defattr(644,root,root,755)

%files i18n-cy -f cy.lang
%defattr(644,root,root,755)

%files i18n-da -f da.lang
%defattr(644,root,root,755)

%files i18n-de -f de.lang
%defattr(644,root,root,755)

%files i18n-dgo -f dgo.lang
%defattr(644,root,root,755)

%files i18n-dz -f dz.lang
%defattr(644,root,root,755)

%files i18n-el -f el.lang
%defattr(644,root,root,755)

%files i18n-en_GB -f en_GB.lang
%defattr(644,root,root,755)

%files i18n-en_ZA -f en_ZA.lang
%defattr(644,root,root,755)

%files i18n-eo -f eo.lang
%defattr(644,root,root,755)

%files i18n-es -f es.lang
%defattr(644,root,root,755)

%files i18n-et -f et.lang
%defattr(644,root,root,755)

%files i18n-eu -f eu.lang
%defattr(644,root,root,755)

%files i18n-fa -f fa.lang
%defattr(644,root,root,755)

%files i18n-fi -f fi.lang
%defattr(644,root,root,755)

%files i18n-fr -f fr.lang
%defattr(644,root,root,755)

%files i18n-ga -f ga.lang
%defattr(644,root,root,755)

%files i18n-gd -f gd.lang
%defattr(644,root,root,755)

%files i18n-gl -f gl.lang
%defattr(644,root,root,755)

%files i18n-gu -f gu.lang
%defattr(644,root,root,755)

%files i18n-gug -f gug.lang
%defattr(644,root,root,755)

%files i18n-he -f he.lang
%defattr(644,root,root,755)

%files i18n-hi -f hi.lang
%defattr(644,root,root,755)

%files i18n-hr -f hr.lang
%defattr(644,root,root,755)

%files i18n-hsb -f hsb.lang
%defattr(644,root,root,755)

%files i18n-hu -f hu.lang
%defattr(644,root,root,755)

%files i18n-id -f id.lang
%defattr(644,root,root,755)

%files i18n-is -f is.lang
%defattr(644,root,root,755)

%files i18n-it -f it.lang
%defattr(644,root,root,755)

%files i18n-ja -f ja.lang
%defattr(644,root,root,755)

%files i18n-ka -f ka.lang
%defattr(644,root,root,755)

%files i18n-kk -f kk.lang
%defattr(644,root,root,755)

%files i18n-km -f km.lang
%defattr(644,root,root,755)

%files i18n-kmr-Latn -f kmr_Latn.lang
%defattr(644,root,root,755)

%files i18n-kn_IN -f kn.lang
%defattr(644,root,root,755)

%files i18n-ko -f ko.lang
%defattr(644,root,root,755)

%files i18n-kok -f kok.lang
%defattr(644,root,root,755)

%files i18n-ks -f ks.lang
%defattr(644,root,root,755)

%files i18n-lb -f lb.lang
%defattr(644,root,root,755)

%files i18n-lo -f lo.lang
%defattr(644,root,root,755)

%files i18n-lt -f lt.lang
%defattr(644,root,root,755)

%files i18n-lv -f lv.lang
%defattr(644,root,root,755)

%files i18n-mai -f mai.lang
%defattr(644,root,root,755)

%files i18n-mk -f mk.lang
%defattr(644,root,root,755)

%files i18n-ml -f ml.lang
%defattr(644,root,root,755)

%files i18n-mn -f mn.lang
%defattr(644,root,root,755)

%files i18n-mni -f mni.lang
%defattr(644,root,root,755)

%files i18n-mr -f mr.lang
%defattr(644,root,root,755)

%files i18n-my -f my.lang
%defattr(644,root,root,755)

%files i18n-nb -f nb.lang
%defattr(644,root,root,755)

%files i18n-ne -f ne.lang
%defattr(644,root,root,755)

%files i18n-nl -f nl.lang
%defattr(644,root,root,755)

%files i18n-nn -f nn.lang
%defattr(644,root,root,755)

%files i18n-nr -f nr.lang
%defattr(644,root,root,755)

%files i18n-nso -f nso.lang
%defattr(644,root,root,755)

%files i18n-oc -f oc.lang
%defattr(644,root,root,755)

%files i18n-om -f om.lang
%defattr(644,root,root,755)

%files i18n-or -f or.lang
%defattr(644,root,root,755)

%files i18n-pa_IN -f pa_IN.lang
%defattr(644,root,root,755)

%files i18n-pl -f pl.lang
%defattr(644,root,root,755)

%files i18n-pt -f pt.lang
%defattr(644,root,root,755)

%files i18n-pt_BR -f pt_BR.lang
%defattr(644,root,root,755)

%files i18n-ro -f ro.lang
%defattr(644,root,root,755)

%files i18n-ru -f ru.lang
%defattr(644,root,root,755)

%files i18n-rw -f rw.lang
%defattr(644,root,root,755)

%files i18n-sa_IN -f sa_IN.lang
%defattr(644,root,root,755)

%files i18n-sat -f sat.lang
%defattr(644,root,root,755)

%files i18n-sd -f sd.lang
%defattr(644,root,root,755)

%files i18n-si -f si.lang
%defattr(644,root,root,755)

%files i18n-sid -f sid.lang
%defattr(644,root,root,755)

%files i18n-sk -f sk.lang
%defattr(644,root,root,755)

%files i18n-sl -f sl.lang
%defattr(644,root,root,755)

%files i18n-sq -f sq.lang
%defattr(644,root,root,755)

%files i18n-sr -f sr.lang
%defattr(644,root,root,755)

%files i18n-sr-Latn -f sr_Latn.lang
%defattr(644,root,root,755)

%files i18n-ss -f ss.lang
%defattr(644,root,root,755)

%files i18n-st -f st.lang
%defattr(644,root,root,755)

%files i18n-sv -f sv.lang
%defattr(644,root,root,755)

%files i18n-sw_TZ -f sw_TZ.lang
%defattr(644,root,root,755)

%files i18n-ta -f ta.lang
%defattr(644,root,root,755)

%files i18n-te -f te.lang
%defattr(644,root,root,755)

%files i18n-tg -f tg.lang
%defattr(644,root,root,755)

%files i18n-th -f th.lang
%defattr(644,root,root,755)

%files i18n-tn -f tn.lang
%defattr(644,root,root,755)

%files i18n-tr -f tr.lang
%defattr(644,root,root,755)

%files i18n-ts -f ts.lang
%defattr(644,root,root,755)

%files i18n-tt -f tt.lang
%defattr(644,root,root,755)

%files i18n-ug -f ug.lang
%defattr(644,root,root,755)

%files i18n-uk -f uk.lang
%defattr(644,root,root,755)

%files i18n-uz -f uz.lang
%defattr(644,root,root,755)

%files i18n-ve -f ve.lang
%defattr(644,root,root,755)

%files i18n-vec -f vec.lang
%defattr(644,root,root,755)

%files i18n-vi -f vi.lang
%defattr(644,root,root,755)

%files i18n-xh -f xh.lang
%defattr(644,root,root,755)

%files i18n-zh_CN -f zh_CN.lang
%defattr(644,root,root,755)

%files i18n-zh_TW -f zh_TW.lang
%defattr(644,root,root,755)

%files i18n-zu -f zu.lang
%defattr(644,root,root,755)
%endif

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}.sh

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/ui-previewer
%dir %{_datadir}/%{name}/share/glade
%{_datadir}/%{name}/share/glade/libreoffice-catalog.xml
