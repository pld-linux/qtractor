# TODO: VST support?, clap
#
# Conditional build:
%bcond_with	sse	# SSE instructions/SSE math
%bcond_without	suil	# SUIL support
%bcond_with	qt5	# Qt5 instead of Qt6

%ifarch %{x8664} x32 pentium3 pentium4
%define	with_sse	1
%endif
%if %{without qt5}
# "Disable libsuil upon Qt >= 6.0.0" in CMakeLists.txt
%undefine	with_suil
%endif
Summary:	Audio/MIDI multi-track sequencer
Summary(pl.UTF-8):	Wielościeżkowy sekwencer dźwięku/MIDI
Name:		qtractor
Version:	1.5.8
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/qtractor/%{name}-%{version}.tar.gz
# Source0-md5:	47e7f4e28a5b15493008acded0f54a39
URL:		https://qtractor.sourceforge.io/
%if %{with qt5}
BuildRequires:	Qt5Gui-devel >= 5.1
BuildRequires:	Qt5Network-devel >= 5.1
BuildRequires:	Qt5Svg-devel >= 5.1
BuildRequires:	Qt5Widgets-devel >= 5.1
BuildRequires:	Qt5Xml-devel >= 5.1
BuildRequires:	Qt5X11Extras-devel >= 5.1
%else
BuildRequires:	Qt6Gui-devel >= 6
BuildRequires:	Qt6Network-devel >= 6
BuildRequires:	Qt6Svg-devel >= 6
BuildRequires:	Qt6Widgets-devel >= 6
BuildRequires:	Qt6Xml-devel >= 6
%endif
BuildRequires:	alsa-lib-devel
BuildRequires:	aubio-devel >= 0.4.1
BuildRequires:	cmake >= 3.15
BuildRequires:	dssi-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	jack-audio-connection-kit-devel >= 0.100.0
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libvorbis-devel
BuildRequires:	libxcb-devel
BuildRequires:	lilv-devel
BuildRequires:	lv2-devel
BuildRequires:	pkgconfig
%if %{with qt5}
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-linguist >= 5
%else
BuildRequires:	qt6-build >= 6
BuildRequires:	qt6-linguist >= 6
%endif
BuildRequires:	rubberband-devel >= 3.0.0
%{?with_suil:BuildRequires:	suil-devel}
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires(post,postun):	gtk-update-icon-cache
Requires:	aubio >= 0.4.1
Requires:	hicolor-icon-theme
Requires:	jack-audio-connection-kit-libs >= 0.100.0
Requires:	rubberband-libs >= 3.0.0
%if %{with sse}
Requires:	cpuinfo(sse)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio/MIDI multi-track sequencer.

%description -l pl.UTF-8
Wielościeżkowy sekwencer dźwięku/MIDI.

%prep
%setup -q

%build
%cmake -B build \
	%{?with_qt5:-DCONFIG_QT6=OFF} \
	%{!?with_sse:-DCONFIG_SSE=OFF} \
	%{!?with_suil:-DCONFIG_LIBSUIL=OFF} \

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.VST2 TRANSLATORS
%attr(755,root,root) %{_bindir}/qtractor
%dir %{_libdir}/qtractor
%attr(755,root,root) %{_libdir}/qtractor/qtractor_plugin_scan
%{_datadir}/mime/packages/org.rncbc.qtractor.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/audio
%{_datadir}/%{name}/instruments
%{_datadir}/%{name}/palette
%dir %{_datadir}/%{name}/translations
%lang(cs) %{_datadir}/%{name}/translations/qtractor_cs.qm
%lang(de) %{_datadir}/%{name}/translations/qtractor_de.qm
%lang(es) %{_datadir}/%{name}/translations/qtractor_es.qm
%lang(fr) %{_datadir}/%{name}/translations/qtractor_fr.qm
%lang(it) %{_datadir}/%{name}/translations/qtractor_it.qm
%lang(ja) %{_datadir}/%{name}/translations/qtractor_ja.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/qtractor_pt_BR.qm
%lang(ru) %{_datadir}/%{name}/translations/qtractor_ru.qm
%lang(uk) %{_datadir}/%{name}/translations/qtractor_uk.qm
%{_datadir}/metainfo/org.rncbc.qtractor.metainfo.xml
%{_desktopdir}/org.rncbc.qtractor.desktop
%{_iconsdir}/hicolor/*x*/apps/org.rncbc.qtractor.png
%{_iconsdir}/hicolor/*x*/mimetypes/org.rncbc.qtractor.application-x-qtractor-*.png
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.qtractor.svg
%{_iconsdir}/hicolor/scalable/mimetypes/org.rncbc.qtractor.application-x-qtractor-*.svg
%{_mandir}/man1/qtractor.1*
%lang(fr) %{_mandir}/fr/man1/qtractor.1*
