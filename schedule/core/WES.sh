dragen -f -r ${1} -1 ${2} -2 ${3} \
--output-file-prefix ${4} \
--output-directory ${5} \
--RGID RGID --RGSM ${4} \
--enable-map-align true \
--enable-map-align-output true \
--output-format bam --enable-sort true \
--enable-duplicate-marking true \
--enable-variant-caller true \
--enable-vcf-compression true \
--vc-target-bed ${6} --vc-target-bed-padding 50 \
--enable-cnv true \
--cnv-target-bed ${6} --cnv-normals-list ${7} \
--enable-sv true --sv-exome true --sv-call-regions-bed ${6}