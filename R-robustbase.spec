%global packname  robustbase
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          0.9.7
Release:          1
Summary:          Basic Robust Statistics
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/robustbase_0.9-7.tar.gz
Requires:         R-stats R-graphics R-methods 
Requires:         R-MASS R-lattice R-boot R-MPV R-xtable R-ggplot2 R-RColorBrewer 
Requires:         R-reshape2
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-graphics R-methods
BuildRequires:    R-MASS R-lattice R-boot R-MPV R-xtable R-ggplot2 R-RColorBrewer 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel
BuildRequires:    R-reshape2

%description
"Essential" Robust Statistics.  The goal is to provide tools allowing to
analyze data with robust methods.  This includes regression methodology
including model selections and multivariate statistics where we strive to
cover the book "Robust Statistics, Theory and Methods" by Maronna, Martin
and Yohai; Wiley 2006.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/Copyrights
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/xtraR


%changelog
* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8_0-1
+ Revision: 777165
- Import R-robustbase
- Import R-robustbase


