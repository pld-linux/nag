Summary:	LDP Network Administrator's Guide
Summary(fr):	Guide de l'administrateur réseau du LDP
Summary(de):	LDP-Netzwerk-Administrator-Handbuch 
Summary(pl):	Podrêcznik Administratora Sieci LDP
Summary(tr):	LDP - NAG, Að yöneticisinin el kitabý
Name:		nag
Version:	1.0
Release:	4
Group:		Documentation
Group(pl):	Dokumentacja
Source:		http://sunsite.unc.edu/LDP/nag.html.tar.gz
Copyright:	distributable
BuildArch:	noarch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a generic guide to the Network Administration of Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr
Guide générique à l'administration réseau sous Linux. 
Allez sur http://sunsite.unc.edu/LDP pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises à jour éventuelles
de cette version.

%description -l de
Dies ist eine allgemeine Anleitung zur Netzwerkverwaltung von Linux-Systemen.
Unter http://sunsite.unc.edu/LDP finden Sie weitere Informationen über das 
Linux Documentation Project und ggf. Updates zu dieser Version.

%description -l pl
To jest ogólny przewodnik po Administracji Sieciami Linuxowymi. Wiêcej
informacji na temat Projektu Dokumentacji Linuxa (LDP) oraz uaktualnienia
tego dokumentu mo¿esz znale¼æ pod adresem http://sunsite.unc.edu/LDP.

%description -l tr
Bu kitap, LDP (Linux belgeleme çalýþmasý) sonucunda ortaya çýkan eserlerden
biri. Serinin diðer kitaplarý ile birlikte bu kitaplarýn güncel bir yansýsýna
http://www.linux.org.tr/LDP altýndan eriþebilirsiniz. Að yöneticisinin el
kitabý Linux'da að hizmetlerinin yönetimi üzerine genel bilgileri içerir.

%prep
%setup -q -n nag

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/doc/LDP/nag

cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/nag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)

/usr/doc/LDP/nag

%changelog
* Mon Feb  8 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.0-4]
- sloted BuildRoot into PLD standard
- simplification in %files
- added -q parameter for %setup

* Sat Feb  6 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.0-3]
- added pl translations
- replaced "mkdir -p" with "install -d"
- rewrote %files section
- changed BuildRoot
- simplification in %install
- moved %changelog to the end of spec
- cosmetic changes

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- created the package
