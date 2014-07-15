%define	pkgname symband

Summary:	Octave package for handling symmetric banded matrices
Name:       octave-%{pkgname}
Version:	1.0.10
Release:	5
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/symband/
BuildRequires:  octave-devel >= 2.9.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Octave package for handling symmetric banded matrices.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}
