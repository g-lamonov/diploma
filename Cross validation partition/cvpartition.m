clear all 
close all
clc

addpath("lib");
addpath("BPSO");

d = 'spam';
populAlg = 50;
iterAlg = 1000;

% Code
% Extraction and normalization of data
% Assignment Xtra and Ytra dataset. Xtra contains
% Xtra provides a set of data
% Ytra contains the classification value

kfold = 10;
species = categorical(Ytra);

err_szt = @(err, nterms, nrule)0.9*err + ...
    0.05*nterms + 0.05*nrule;

fold=cvpartition(species, 'kfold', kfold);
for i=1:kfold
    trainIdx=fold.training(i);
    testIdx=fold.test(i);
    Xtra2=Xtra(trainIdx,:);
    Ytra2=Ytra(trainIdx);

    Xtst2=Xtra(testIdx,:);
    Ytst2=Ytra(testIdx);

    %====================== BDA ======================
    optfun =  @(fobj,sizesol, niter, npopul, des, uppbound)...
    BDA(npopul,niter,sizesol,fobj, i);
    
    [fis, score, curve] = genfisdiscr(Xtra2, Ytra2, populAlg, iterAlg, 'gaussmf' , 5, ...
        true, true, optfun, err_szt);
    %ruleview(ConvertToFis(fis));
    out_tra = evalcfisW(Xtra2, fis, 'gaussmf');
    out_tst = evalcfisW(Xtst2, fis, 'gaussmf');
    disp(['Точность на обучающих данных ' num2str(mean(out_tra==Ytra2))]);
    disp(['Точность на тестовых данных ' num2str(mean(out_tst==Ytst2))]);
    fprintf('Terms: ');
    disp(sum([fis.rule.antecedent]~=0));
    fprintf('Rules: ');
    disp({fis(:).rule});
    fprintf('');
    
    %====================== BAM ======================
    optfun =  @(fobj,sizesol, niter, npopul, des, uppbound)...
    BAM(npopul, niter, sizesol, 1, fobj, 0, i);

    [fis, score, curve] = genfisdiscr(Xtra2, Ytra2, populAlg, iterAlg, 'gaussmf' , 5, ...
        true, true, optfun, err_szt);
    %ruleview(ConvertToFis(fis));
    out_tra = evalcfisW(Xtra2, fis, 'gaussmf');
    out_tst = evalcfisW(Xtst2, fis, 'gaussmf');
    disp(['Точность на обучающих данных ' num2str(mean(out_tra==Ytra2))]);
    disp(['Точность на тестовых данных ' num2str(mean(out_tst==Ytst2))]);
    fprintf('Terms: ');
    disp(sum([fis.rule.antecedent]~=0));
    fprintf('Rules: ');
    disp({fis(:).rule});
    fprintf('');
    
    %====================== BPSO ======================
    optfun =  @(fobj,sizesol, niter, npopul, des, uppbound)...
    BPSO(npopul,niter,2,fobj,sizesol, i); 

    [fis, score, curve] = genfisdiscr(Xtra2, Ytra2, populAlg, iterAlg, 'gaussmf' , 5, ...
        true, true, optfun, err_szt);
    %ruleview(ConvertToFis(fis));
    out_tra = evalcfisW(Xtra2, fis, 'gaussmf');
    out_tst = evalcfisW(Xtst2, fis, 'gaussmf');
    disp(['Точность на обучающих данных ' num2str(mean(out_tra==Ytra2))]);
    disp(['Точность на тестовых данных ' num2str(mean(out_tst==Ytst2))]);
    fprintf('Terms: ');
    disp(sum([fis.rule.antecedent]~=0));
    fprintf('Rules: ');
    disp({fis(:).rule});
    fprintf('');
    
    %====================== BBA ======================
    optfun =  @(fobj,sizesol, niter, npopul, des, uppbound)...
    BBA(npopul,0.9, 0.9, sizesol,niter, fobj, i);
    
    [fis, score, curve] = genfisdiscr(Xtra2, Ytra2, populAlg, iterAlg, 'gaussmf' , 5, ...
        true, true, optfun, err_szt);
    %ruleview(ConvertToFis(fis));
    out_tra = evalcfisW(Xtra2, fis, 'gaussmf');
    out_tst = evalcfisW(Xtst2, fis, 'gaussmf');
    disp(['Точность на обучающих данных ' num2str(mean(out_tra==Ytra2))]);
    disp(['Точность на тестовых данных ' num2str(mean(out_tst==Ytst2))]);
    fprintf('Terms: ');
    disp(sum([fis.rule.antecedent]~=0));
    fprintf('Rules: ');
    disp({fis(:).rule});
    fprintf('');
end