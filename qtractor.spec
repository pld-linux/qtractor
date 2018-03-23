Summary:	Audio/MIDI multi-track sequencer
Summary(pl.UTF-8):	Wielościeżkowy sekwencer dźwięku/MIDI
Name:		qtractor
Version:	0.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/qtractor/%{name}-%{version}.tar.gz
# Source0-md5:	e8b1955b29abbe84e94d7ed05d260b8d
URL:		https://qtractor.sourceforge.io/
BuildRequires:	Qt5Gui-devel >= 5.1
BuildRequires:	Qt5Xml-devel >= 5.1
BuildRequires:	alsa-lib-devel
BuildRequires:	dssi-devel
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lilv-devel
BuildRequires:	lv2-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	rubberband-devel
BuildRequires:	suil-devel
BuildRequires:	zlib-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libX11-devel
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio/MIDI multi-track sequencer.

%description -l pl.UTF-8
Wielościeżkowy sekwencer dźwięku/MIDI.

%prep
%setup -q

%build
%{__autoheader}
%{__autoconf}
%configure \
	--with-qt5=%{_libdir}/qt5 \
	--enable-lilv	\
	--enable-suil	\
	--localedir=%{_datadir}/%{name}/translations

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/qtractor
%attr(755,root,root) %{_bindir}/qtractor_plugin_scan
%{_mandir}/man1/qtractor.1*
%lang(fr) %{_mandir}/man1/qtractor.fr.1*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/mime/packages/qtractor.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/metainfo/qtractor.appdata.xml
