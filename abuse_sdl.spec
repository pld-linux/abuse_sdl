Summary:	An SDL port of the game Abuse
Summary(pl):	Port SDL gry Abuse
Name:		abuse_sdl
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
#Source0Download: http://www.labyrinth.net.au/~trandor/abuse/
Source0:	http://www.labyrinth.net.au/~trandor/abuse/files/%{name}-%{version}.tar.bz2
# Source0-md5:	59ea4498886642aa975f04233cc92558
Source1:	http://www.labyrinth.net.au/~trandor/abuse/files/abuse_datafiles.tar.gz
# Source1-md5:	2b857668849b2dc7cd29cdd84a33c19e
Source2:	%{name}.desktop
Patch0:		%{name}-etc_dir.patch
URL:		http://www.labyrinth.net.au/~trandor/abuse/
BuildRequires:	SDL-devel >= 1.1.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_abusedir	%{_datadir}/games/abuse

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%description -l pl
Abuse-SDL to port Abuse, klasycznej gry Crack-Dot-Com, dla biblioteki
SDL. Mo¿e dzia³aæ w dowolnej g³êbi koloru, w okienku lub na pe³nym
ekranie, ma d¼wiêk stereo z panningiem.

%prep
%setup -q -a 1
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir},%{_abusedir}/{art,addon,levels,lisp,music,netlevel,register,sfx}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install abuse.png $RPM_BUILD_ROOT%{_pixmapsdir}

cp -R art	$RPM_BUILD_ROOT%{_abusedir}
cp -R addon	$RPM_BUILD_ROOT%{_abusedir}
cp -R levels	$RPM_BUILD_ROOT%{_abusedir}
cp -R lisp	$RPM_BUILD_ROOT%{_abusedir}
cp -R music	$RPM_BUILD_ROOT%{_abusedir}
cp -R netlevel	$RPM_BUILD_ROOT%{_abusedir}
cp -R register	$RPM_BUILD_ROOT%{_abusedir}
cp -R sfx	$RPM_BUILD_ROOT%{_abusedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README* TODO
%attr(755,root,root) %{_bindir}/*
# can't these be simplified?
%dir %{_abusedir}
%{_abusedir}/*.bmp
%{_abusedir}/*.png
%{_abusedir}/*.lsp
%dir %{_abusedir}/sfx
%{_abusedir}/sfx/*.wav
%dir %{_abusedir}/register
%{_abusedir}/register/*
%dir %{_abusedir}/netlevel
%{_abusedir}/netlevel/*.spe
%dir %{_abusedir}/music
%{_abusedir}/music/*
%dir %{_abusedir}/lisp
%{_abusedir}/lisp/*.lsp
%dir %{_abusedir}/levels
%{_abusedir}/levels/*
%dir %{_abusedir}/art
%{_abusedir}/art/*
%dir %{_abusedir}/addon
%dir %{_abusedir}/addon/*
%{_abusedir}/addon/*/*
%{_pixmapsdir}/*.png
%{_applnkdir}/Games/Arcade/*.desktop
%{_mandir}/man6/*.6*
