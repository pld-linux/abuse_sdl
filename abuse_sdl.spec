Summary:	An SDL port of the game Abuse
Summary(pl.UTF-8):   Port SDL gry Abuse
Name:		abuse_sdl
Version:	0.7.0
Release:	3
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
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_abusedir	%{_datadir}/games/abuse

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%description -l pl.UTF-8
Abuse-SDL to port Abuse, klasycznej gry Crack-Dot-Com, dla biblioteki
SDL. Może działać w dowolnej głębi koloru, w okienku lub na pełnym
ekranie, ma dźwięk stereo z panningiem.

%prep
%setup -q -a 1
%patch0 -p1

%build
sed -i -e "s:/usr/local/share/games/abuse:%{_abusedir}:" src/sdlport/setup.cpp
sed -i -e "s:(load \"lisp/ant.lsp\"):(load \"lisp/ant.lsp\")\n(load \"register/ant.lsp\"):" abuse.lsp
cp /usr/share/automake/config.sub .

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_abusedir}/{art,addon,levels,lisp,music,netlevel,register,sfx}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install abuse.png $RPM_BUILD_ROOT%{_pixmapsdir}

for dir in art addon levels lisp music netlevel register sfx
do
cp -R $dir $RPM_BUILD_ROOT%{_abusedir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README* TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_abusedir}
%{_abusedir}/*.bmp
%{_abusedir}/*.png
%{_abusedir}/*.lsp
%{_abusedir}/sfx
%{_abusedir}/register
%{_abusedir}/netlevel
%{_abusedir}/music
%{_abusedir}/lisp
%{_abusedir}/levels
%{_abusedir}/art
%{_abusedir}/addon
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man6/*.6*
