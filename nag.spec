Summary:	LDP Network Administrator's Guide
Summary(fr):	Guide de l'administrateur r�seau du LDP
Summary(de):	LDP-Netzwerk-Administrator-Handbuch
Summary(pl):	Podr�cznik Administratora Sieci LDP
Summary(tr):	LDP - NAG, A� y�neticisinin el kitab�
Name:		nag
Version:	2.0
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.linuxdoc.org/LDP/%{name}-%{version}.html.tar.gz
# Source0-md5:	3495e385c001cbc8879c128498246d20
URL:		http://www.linuxdoc.org/LDP/nag2/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic guide to the Network Administration of Linux
systems. Check http://www.linuxdoc.org/ for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr
Guide g�n�rique � l'administration r�seau sous Linux. Allez sur
http://www.linuxdoc.org/ pour plus d'informations sur le Projet de
Documentation Linux (LDP) et les mises � jour �ventuelles de cette
version.

%description -l de
Dies ist eine allgemeine Anleitung zur Netzwerkverwaltung von
Linux-Systemen. Unter http://www.linuxdoc.org/ finden Sie weitere
Informationen �ber das Linux Documentation Project und ggf. Updates zu
dieser Version.

%description -l pl
To jest og�lny przewodnik po Administracji Sieciami Linuksowymi. Wi�cej
informacji na temat Projektu Dokumentacji Linuksa (LDP) oraz
uaktualnienia tego dokumentu mo�esz znale�� pod adresem
http://www.linuxdoc.org/ .

%description -l tr
Bu kitap, LDP (Linux belgeleme �al��mas�) sonucunda ortaya ��kan
eserlerden biri. Serinin di�er kitaplar� ile birlikte bu kitaplar�n
g�ncel bir yans�s�na http://www.linuxdoc.org/ alt�ndan
eri�ebilirsiniz. A� y�neticisinin el kitab� Linux'da a� hizmetlerinin
y�netimi �zerine genel bilgileri i�erir.

%prep
%setup -q -n nag2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LDP/nag

cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LDP/nag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LDP/nag
