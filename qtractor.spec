Summary:	Audio/MIDI multi-track sequencer
Summary(pl.UTF-8):	Wielościeżkowy sekwencer dźwięku/MIDI
Name:		qtractor
Version:	0.5.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qtractor/%{name}-%{version}.tar.gz
# Source0-md5:	22abf4de4d5736f794e174ef06fe3a3c
URL:		http://qtractor.sourceforge.net/
BuildRequires:	QtGui-devel >= 4.2
BuildRequires:	QtXml-devel >= 4.2
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
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	rubberband-devel
BuildRequires:	suil-devel
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
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/32x32/*/*.png
%{_datadir}/mime/packages/qtractor.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.qm
